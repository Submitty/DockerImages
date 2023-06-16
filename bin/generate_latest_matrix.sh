#!/usr/bin/env bash

set -e

# gives the path of the dockerfiles that have been modified/added in the last commit to main
changed_dockerfile_path=$(git diff --name-only $1 $2 | grep '/Dockerfile$')

total_files=$(echo "${changed_dockerfile_path}" | wc -l)

json_file="./latest.json"

# Read the JSON file into a variable
json_data=$(cat "$json_file")

# Extract values using string manipulation and pattern matching
docker_names=$(echo "$json_data" | grep -o '"docker_name":"[^"]*' | awk -F'"' '{print $4}')
docker_tags=$(echo "$json_data" | grep -o '"tag":"[^"]*' | awk -F'"' '{print $4}')

# Convert latest_docker_names to an array
readarray -t latest_docker_names <<< "$docker_names"
readarray -t latest_docker_tags <<< "$docker_tags"

echo -n '{\"include\": ['

# loop over the filepaths to make the context and tag for github action
index=0
for file_path in ${changed_dockerfile_path}; do
    if [[ $file_path =~ ^.*/submitty/[^/]+/[^/]+/Dockerfile$ ]]; then

        docker_tag=$(basename $(dirname "$file_path"))
        docker_name=$(basename $(dirname $(dirname "$file_path")))
        university=$(basename $(dirname $(dirname $(dirname "$file_path"))))

        found=false
        for ((i = 0; i < ${#latest_docker_names[@]}; i++)); do
            if [[ "${latest_docker_names[i]}" == "$docker_name" && "${latest_docker_tags[i]}" == "$docker_tag" ]]; then
                found=true
                break
            fi
        done
        
        # removing the last Dockerfile from the file path
        updated_path=$(echo "$file_path" | sed 's/\/Dockerfile$//')

        if [[ "$found" == true ]]; then
            echo -n '{\"context\": \""'"$updated_path"'"\", \"dockername\": \""'"$docker_name"'"\", \"tag\" :\""'"$docker_tag"'"\"},' # modularize
        fi
    fi
done

echo -n ']}'

