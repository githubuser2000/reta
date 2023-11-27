#!/bin/bash
version=`~/myRepos/reta/libs/version.sh`
#echo $version
sed -i 's/\(version\s*=\s*"\)[^"]*"/\1'${version}'"/g' ~/myRepos/reta/{setup.py,pyproject.toml} > /dev/null 2> /dev/null
