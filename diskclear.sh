#!/bin/bash

DISK_PERCENT=$(df -mh | grep '/dev/sda1\>' | awk '{print $5}' | sed 's/%//g' )
today=`date`


echo $DISK_PERCENT

if [ $DISK_PERCENT -gt 85 ]; then
        echo "[$today] 임시파일 삭제"
        rm -rf 
else
        echo "[$today] 스킵"
fi
