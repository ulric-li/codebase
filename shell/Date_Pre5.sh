#########################################################################
# File Name: Date_Pre5.sh
# Author: Ulric
# mail: 675962721@qq.com
# Created Time: Fri 11 Mar 2016 11:13:24 AM CST
#########################################################################
#!/bin/bash

vdatemn=$1

if [ "$vdatemn" = "" ]
then
	Date_Pre5=`date --date="-10 minute" +%Y%m%d%H%M`
	echo ${Date_Pre5}
	if [ ${Date_Pre5:11:1} -lt 5 ];then
		vdatemn=${Date_Pre5:0:11}0
	else
		vdatemn=${Date_Pre5:0:11}5
	fi
fi

echo ${vdatemn}
