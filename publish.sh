#!/usr/bin/env bash

array=( $(git diff --name-only HEAD~1 HEAD) )
built=()
failed=()
for i in "${array[@]}"; do
    # Check if file exists, that it's under the dockerfiles folder and that the file is named "Dockerfile"
    if [ -f ${i} ] && [[ ${i} == dockerfiles/* ]] && [[ ${i} == */Dockerfile ]]; then
        path=$(echo ${i} | sed 's/\(.*\)\/Dockerfile/\1/g')
        pushd ${path} > /dev/null
        tag=$(jq -r '.hostname' metadata.json)/$(jq -r '.name' metadata.json):$(jq -r '.tag' metadata.json)
        echo -e "Building: ${tag}\n"
        docker build --quiet --tag ${tag} .
        if [ $? -eq 0 ]; then
            built+=(${tag})
            if [ "$TRAVIS_BRANCH" = "master" -a "$TRAVIS_PULL_REQUEST" = "false" ]; then
                docker push ${tag}
            fi
            echo -e "\n==============="
            echo -e "   DONE!"
            echo -e "===============\n"
        else
            failed+=(${tag})
            echo -e "\n==============="
            echo -e "   FAILED!"
            echo -e "===============\n"
        fi
        popd > /dev/null
    fi
done

echo -e "End Status Report"
if [ ${#built[@]} -ne 0 ]; then
    echo -e "  Built"
    for i in "${built[@]}"; do
        printf "\xE2\x9C\x94 ${i}\n"
    done
fi

echo -e "\n"

if [ ${#failed[@]} -ne 0 ]; then
    echo -e "  Failed"
    for i in "${failed[@]}"; do
        echo -e "x ${failed[@]}"
    done
fi