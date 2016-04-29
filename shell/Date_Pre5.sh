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

# 获取指定时间
# 下面命令可以得到20160501的7天前的日期
sev=`date -d"7 day ago 20160501" +%Y%m%d`
echo $sev
