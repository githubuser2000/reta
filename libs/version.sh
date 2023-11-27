#!/bin/sh
commitNum=`git --git-dir=/home/alex/myRepos/reta/.git --work-tree=/home/alex/myRepos/reta log --oneline | less -S | wc -l`
datum=`date +"%Y%m%d"`
echo "3."${datum}"."${commitNum}

