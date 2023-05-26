import json
import os
from pathlib import Path
import random
import re
import sys

# this script finds the metadata.json files and creates a github action file
# with the appropriate steps to build and push the containers to dacker hub
# one of the jobs looks for changed files to only push changed containers

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

# modify tags to ensure names are valid for github actions variable names
tag_vars: dict[str,str] = dict()
def tag_modifier(tag: str):
    global tag_vars
    if tag in tag_vars:
        return tag_vars[tag]
    if re.fullmatch(r'[_A-Za-z][_A-Za-z0-9]*',tag): # name is in proper format
        tag_vars[tag] = tag
        return tag
    else: # try replacing invalid chars
        newtag = ''.join(c if re.fullmatch(r'[_A-Za-z0-9]',c) else '_' for c in tag)
        if not re.fullmatch(r'[_A-Za-z]',newtag[0]):
            newtag = 'tag_' + newtag
        if re.fullmatch(r'[_A-Za-z][_A-Za-z0-9]*',newtag):
            tag_vars[tag] = newtag
            return newtag
        else: # pick something random
            counter = 0 # prevent infinite loop
            while True:
                counter += 1
                newtag = 'tag_' + str(random.randint(100000,999999))
                if newtag not in tag_vars.values():
                    tag_vars[tag] = newtag
                    return newtag
                assert counter < 1000

# output start of the file checking job
def account_job_check(username: str, infos):
    ret = f'''\
  # this job checks which containers for account "{username}" should be updated
  check-files-{username}:
    name: Check modified files ({username})
    runs-on: ubuntu-latest
    # variables that tell which containers should be updated
    outputs:
'''
    for name,tag,dir in infos:
        tag = tag_modifier(tag)
        ret += f'''\
      {name}__{tag}: ${{{{ steps.check-files-{username}.outputs.{name}__{tag} }}}}
'''
    ret += f'''\
    steps:
    - name: Code checkout
      uses: actions/checkout@v3
      with:
        fetch-depth: 2
    - name: Look for modified files
      id: check-files-{username}
      # look for whether any files were modified in the container's directory
      run: |
'''
    for name,tag,dir in infos:
        tag = tag_modifier(tag)
        ret += f'''\
        COUNT=$(git diff --name-only HEAD^ HEAD | grep {dockerhub_accounts[username]}/{name}/ | wc -l)
        if [[ $COUNT != 0 ]]; then echo "{name}__{tag}=true" >> $GITHUB_OUTPUT; else echo "{name}__{tag}=false" >> $GITHUB_OUTPUT; fi;
'''
    return ret

# output the start of a per-account job
def account_job_start(username: str):
    return f'''\
  # this job pushes container images for account "{username}"
  push-images-{username}:
    name: Push docker images ({username})
    runs-on: ubuntu-latest
    needs: check-files-{username}
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
      if: needs.check-files-{username}.outputs.{name}__{tag_modifier(tag)} == 'true'
      uses: docker/build-push-action@releases/v3
      with:
        context: {path}
        push: true
        tags: {username}/{name}:{tag}
'''

# find all metadata.json files and create a job step for each
def process_account(username: str, filepath: str):
    log_err(f'processing docker hub account {username}')
    infos = [] # list of (name,tag,dir)
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
                infos.append((name,tag,dir))
    infos = sorted(infos)
    print(account_job_check(username,infos))
    print(account_job_start(username))
    for name,tag,dir in infos:
        log_err(f'processing {name}:{tag} in {dir}')
        print(account_container_string(username,name,tag,dir))

if __name__ == '__main__':
    print(file_start)
    for username in sorted(dockerhub_accounts.keys()):
        process_account(username,dockerhub_accounts[username])
    if False: # set to True to show tag name mappings
        print('# tag name mapping:')
        for k in tag_vars:
            print('#',k,'->',tag_vars[k])
