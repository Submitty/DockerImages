set -ev

files=( $(git diff --name-only HEAD~1 HEAD) )
for i in "${array[@]}"; do
  if [[ ${i} == dockerfiles/* ]] && [[ ${i} == */Dockerfile ]]; then
    path=$(echo ${i} | sed 's/dockerfiles\/\(.*\)\/Dockerfile/\1/g')
    pushd ${path}
    docker build . -t $(jq -r '.hostname' metadata.json)/$(jq -r '.name' metadata.json):$(jq -r '.tag' metadata.json)
  fi
done