#!/bin/sh
#
for I
    do
	case $I in
	-[abc]) echo ' -a | -b | -c ' ;;
	-x) echo ' -x ' ;;
	*) echo " ??? $I ??? " ;;
	esac
    done
    
    