#!/usr/bin/env bash

echo "${DOCKER_PASSWORD}" | docker login -u "${DOCKER_USERNAME}" --password-stdin

built=()
failed=()
array=( $(git diff --name-only HEAD~1 HEAD) )
for i in "${array[@]}"; do
    # Check if file exists, that it's under the dockerfiles folder and that the file is named "Dockerfile"
    if [ -f ${i} ] && [[ ${i} == dockerfiles/* ]] && [[ ${i} == */Dockerfile ]]; then
        path=$(echo ${i} | sed 's/\(.*\)\/Dockerfile/\1/g')
        pushd ${path} > /dev/null
        docker_tag=$(jq -r '.hostname' metadata.json)/$(jq -r '.name' metadata.json):$(jq -r '.tag' metadata.json)
        echo -e "Publishing: ${docker_tag}\n"
        docker push ${docker_tag}
        if [ $? -eq 0 ]; then
            built+=(${docker_tag})
        else
            failed+=(${docker_tag})
        fi
        popd > /dev/null
    fi
done

echo -e "End Publish Status Report"
if [ ${#built[@]} -ne 0 ]; then
    echo -e "  Pushed"
    for i in "${built[@]}"; do
        printf "    ${ANSI_GREEN}\xE2\x9C\x94${ANSI_RESET} ${i}\n"
    done
fi

echo -e "\n"

if [ ${#failed[@]} -ne 0 ]; then
    echo -e "  Failed"
    for i in "${failed[@]}"; do
        echo -e "    ${ANSI_RED}x${ANSI_RESET} ${failed[@]}"
    done
    exit 1
fi