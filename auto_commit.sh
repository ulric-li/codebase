#!/usr/bin/env bash

###################################################################
# AUTHOR:	montella_li
# DATE:		2016-04-01
# EMAIL:	532828145@qq.com
# PURPOSE:	将本地练习的脚本在下班前自动提交到github
#
# HISTORY:
# 2016-04-01				montella_li				New Application
####################################################################

commit_time=`date`
cd /home/montella/codebase
git add *
git commit -m "auto commit local code to github at $commit_time"
git push
