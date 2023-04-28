import json
import os
from pathlib import Path
import sys

# this script finds the metadata.json files and creates a github action file
# with the appropriate steps to build and push the containers to dacker hub

# to use this script run this in the repository root:
# python3 make_github_action.py > .github/workflows/dockerhub_push.yml

def log_err(a: str):
    sys.stderr.write(a+'\n')

# top of the github actions file
file_start = '''\
name: Push to Docker Hub

on:
  push:
    branches:
    - main

jobs:
'''

# dictionary mapping docker hub username/hostname to
# a directory in this repository with the dockerfiles
dockerhub_accounts = {
    'submitty': 'dockerfiles/submitty',
    'submittyrpi': 'dockerfiles/submittyrpi'
}

# output the start of a per-account job
def account_job_start(username: str):
    return f'''\
  push-images-{username}:
    name: Push docker images ({username})
    runs-on: ubuntu-latest
    steps:
    - name: Check out repo
      uses: actions/checkout@v3
    - name: Docker Hub login
      uses: docker/login-action@releases/v1
      with:
        username: ${{{{ secrets.DOCKER_USERNAME_{username.upper()} }}}}
        password: ${{{{ secrets.DOCKER_PASSWORD_{username.upper()} }}}}
'''

# output a job step for pushing a container
def account_container_string(username: str, name: str, tag: str, path: str):
    return f'''\
    - name: Build and push {username}/{name}:{tag}
      uses: docker/build-push-action@releases/v3
      with:
        context: {path}
        push: true
        tags: {username}/{name}:{tag}
'''

print(file_start)

# find all metadata.json files and create a job step for each
def process_account(username: str, filepath: str):
    log_err(f'processing docker hub account {username}')
    # traverse the directory tree in sorted order to keep diff sizes small
    for dir,subdirs,files in sorted(os.walk(filepath)):
        if 'metadata.json' in files:
            log_err(f'found metadata file {dir}/metadata.json')
            with open(Path(dir,'metadata.json'),'r') as metafile:
                metadata = json.load(metafile)
                # docker hub username/hostname should match
                assert metadata['hostname'] == username
                name = metadata['name']
                tag = metadata['tag']
                print(account_container_string(username,name,tag,dir))

for username in sorted(dockerhub_accounts.keys()):
    print(account_job_start(username))
    process_account(username,dockerhub_accounts[username])
