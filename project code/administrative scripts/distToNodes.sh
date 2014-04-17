#!/bin/bash 


if [ $# -ne 2 ]
then 
echo "distFileToNodes.sh: Incorrect number of arguments!"
echo "./distFileToAllNodes.sh -[File To Distribute] [location to distribute to]"
exit 1
fi

#Head node is not included in the transfer
scp $1 pi@192.168.0.102:$2
scp $1 pi@192.168.0.103:$2
scp $1 pi@192.168.0.104:$2

exit 0