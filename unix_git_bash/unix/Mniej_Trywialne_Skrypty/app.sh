#!/bin/sh
#
case $# in
    1) cat >> $1 ;;
    2) cat >>$2 <$1 ;;
    *) echo "Usage: $0 [file1] file2" ;;
esac
