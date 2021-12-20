#!/bin/bash

for (( ; ; ))
do
	echo Cierpienie trwa już `awk '{print int($1/3600)":"int(($1%3600)/60)":"int($1%60)}' /proc/uptime`
	sleep 1
done
