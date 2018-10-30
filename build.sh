#!/usr/bin/env bash

# These functions and stuff are taken from https://github.com/travis-ci/travis-build/tree/master/lib/travis/build/bash
export ANSI_RED="\033[31;1m"
export ANSI_GREEN="\033[32;1m"
export ANSI_YELLOW="\033[33;1m"
export ANSI_RESET="\033[0m"
export ANSI_CLEAR="\033[0K"

travis_nanoseconds() {
  local cmd='date'
  local format='+%s%N'

  if hash gdate >/dev/null 2>&1; then
    cmd='gdate'
  elif [[ "${TRAVIS_OS_NAME}" == osx ]]; then
    format='+%s000000000'
  fi

  "${cmd}" -u "${format}"
}

travis_fold() {
  local action="${1}"
  local name="${2}"
  echo -en "travis_fold:${action}:${name}\\r${ANSI_CLEAR}"
}

travis_time_start() {
  TRAVIS_TIMER_ID="$(printf %08x $((RANDOM * RANDOM)))"
  TRAVIS_TIMER_START_TIME="$(travis_nanoseconds)"
  export TRAVIS_TIMER_ID TRAVIS_TIMER_START_TIME
  echo -en "travis_time:start:$TRAVIS_TIMER_ID\\r${ANSI_CLEAR}"
}

travis_time_finish() {
  local result="${?}"
  local travis_timer_end_time
  travis_timer_end_time="$(travis_nanoseconds)"
  local duration
  duration="$((travis_timer_end_time - TRAVIS_TIMER_START_TIME))"
  echo -en "\\ntravis_time:end:${TRAVIS_TIMER_ID}:start=${TRAVIS_TIMER_START_TIME},finish=${travis_timer_end_time},duration=${duration}\\r${ANSI_CLEAR}"
  return "${result}"
}
#set -ev

array=( $(git diff --name-only HEAD~1 HEAD) )
built=()
failed=()
for i in "${array[@]}"; do
    # Check if file exists, that it's under the dockerfiles folder and that the file is named "Dockerfile"
    if [ -f ${i} ] && [[ ${i} == dockerfiles/* ]] && [[ ${i} == */Dockerfile ]]; then
        path=$(echo ${i} | sed 's/\(.*\)\/Dockerfile/\1/g')
        pushd ${path} > /dev/null
        hostname=$(jq -r '.hostname' metadata.json)
        name=$(jq -r '.name' metadata.json)
        tag=$(jq -r '.tag' metadata.json)
        travis_tag=${hostname}_${name}_${tag}
        docker_tag=${hostname}/${name}:${tag}
        travis_fold start docker.build ${travis_tag}
        travis_time_start
        echo -e "Building: ${docker_tag}\n"
        docker build --quiet --tag ${docker_tag} .
        if [ $? -eq 0 ]; then
            built+=(${docker_tag})
            echo -e "\n==============="
            echo -e "   DONE!"
            echo -e "===============\n"
        else
            failed+=(${docker_tag})
            echo -e "\n==============="
            echo -e "   FAILED!"
            echo -e "===============\n"
        fi
        travis_time_finish
        travis_fold end docker.build ${travis_tag}
        popd > /dev/null
    fi
done

echo -e "End Build Status Report"
if [ ${#built[@]} -ne 0 ]; then
    echo -e "  Built"
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
