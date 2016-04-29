#########################################################################
# File Name: a.sh
# Author: Ulric
# mail: 675962721@qq.com
# Created Time: Thu 28 Apr 2016 05:48:32 PM CST
#########################################################################
#!/usr/bin/env bash

shname=`basename $0`
processNumLimit=$1

if [ $# -ne 1 ]
then
	echo "Usage: ${shname} processNumLimit"
	echo "参数1：<进程最大数量>超过此数量，进程退出"
	exit 1
fi

if [ `ps aux | grep ${shname} | grep -v grep | wc -l` -gt ${processNumLimit} ]
then
	echo "进程数过多，预计存在积压，请检查"
	exit 1
fi
