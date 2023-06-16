#!/usr/bin/env bash

set -e

# # gives the path of the dockerfiles that have been modified/added in the last commit to main
changed_dockerfile_path=$(git diff --name-only $1 $2 | grep '/Dockerfile$')
total_files=$(echo "${changed_dockerfile_path}" | wc -l)

echo -n '{\"include\": ['

# loop over the filepaths to make the context and tag for github action
index=0
for file_path in ${changed_dockerfile_path}; do
    if [[ $file_path =~ ^.*/submitty/[^/]+/[^/]+/Dockerfile$ ]]; then

        docker_tag=$(basename $(dirname "$file_path"))
        docker_name=$(basename $(dirname $(dirname "$file_path")))
        university=$(basename $(dirname $(dirname $(dirname "$file_path"))))

        # removing the last Dockerfile from the file path
        updated_path=$(echo "$file_path" | sed 's/\/Dockerfile$//')

        echo -n '{\"context\": \""'"$updated_path"'"\", \"dockername\": \""'"$docker_name"'"\", \"tag\" :\""'"$docker_tag"'"\"},' # modularize
    fi
done

echo -n ']}'
