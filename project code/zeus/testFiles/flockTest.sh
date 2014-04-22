#!/bin/bash 
lockFile="/home/nedwards/pi/algo2/Mesgs/msgs.txt"


(
flock -e 200

while [ 1 -eq 1 ]
do

echo "msg file should  be locked: $lockFile"
sleep 5


done
) 200>$lockFile


exit




