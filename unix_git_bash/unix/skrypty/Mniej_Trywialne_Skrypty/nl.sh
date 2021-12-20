#!/bin/sh
# Check if any parameters present
if [ "$#" -eq 0 ]
then
     echo "Usage: $0 file"
     exit 1
fi
# Process each file
LNUM=1
for FILE
do
     # Make sure file exists
     if [ ! -f "$FILE" ]
     then
          echo "$FILE: non-existent or not accessible"
          exit 1
     fi
     # Read each line, display with line number
     cat $FILE | while read LINE
     do
          echo "$LNUM: $LINE"
          LNUM=`expr $LNUM + 1`
     done
     # Reset line number counter
     LNUM=1
done
