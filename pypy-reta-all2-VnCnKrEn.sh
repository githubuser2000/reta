#!/bin/bash
SCRIPT_PATH="${BASH_SOURCE:-$0}"
ABS_SCRIPT_PATH="$(realpath "${SCRIPT_PATH}")"
#ABS_DIRECTORY="$(dirname "${ABS_SCRIPT_PATH}")"
ABS_DIRECTORY="/home/alex/Eigene-Dateien/myRepos/reta"
GIT_DIRECTORY="${ABS_DIRECTORY}/.git"
${ABS_DIRECTORY}/libs/changeVersion.sh
function ctrl_c() {
    cat ${ABS_DIRECTORY}/head1.alx
    cat ${ABS_DIRECTORY}/religionen.js | sed 's/Grundstrukturen/basic_structures/g'
    cat ${ABS_DIRECTORY}/head2.alx
    cat ~/middle-${2}.alx
    pypy3 ${ABS_DIRECTORY}/grundStrukHtml.py blank
    pypy3 ${ABS_DIRECTORY}/grundStrukHtml.py blank -language=${2}
    cat ${ABS_DIRECTORY}/footer.alx
}
trap ctrl_c INT
if [ "$1" == 'reta' ]; then
	pypy3 ${ABS_DIRECTORY}/reta -columns --all --width=0 -output --type=html --onetable --nocolor -language=${2} >  ~/middle-${2}.alx
fi
#chown -R alex:alex ${ABS_DIRECTORY}
ctrl_c ${1} ${2}
