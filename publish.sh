#!/usr/bin/env bash

array=( $(git diff --name-only HEAD~1 HEAD) )
for i in "${array[@]}"; do
    # Check if file exists, that it's under the dockerfiles folder and that the file is named "Dockerfile"
    if [ -f ${i} ] && [[ ${i} == dockerfiles/* ]] && [[ ${i} == */Dockerfile ]]; then
        path=$(echo ${i} | sed 's/\(.*\)\/Dockerfile/\1/g')
        pushd ${path} > /dev/null
        tag=$(jq -r '.hostname' metadata.json)/$(jq -r '.name' metadata.json):$(jq -r '.tag' metadata.json)
        echo -e "Building: ${tag}\n"
        docker build . -t ${tag}
        docker push ${tag}
        echo -e "\n==============="
        echo -e "   DONE!"
        echo -e "===============\n"
        popd > /dev/null
    fi
done