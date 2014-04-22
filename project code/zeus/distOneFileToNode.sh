#!/bin/bash 

######### TO DO ##########################
#1.Make sure file runs


#############################################################
# Aurthor Nicolas Edwards
#Script takes in: 
#
#arg1=filename to be sent
#arg2=ip address to send to
#This file will be ran by head node to distribute code to 
#the node computers.
#
#File will be placed in /home/pi/algo2/transferedFiles/ for use by the node later
#################################################################################

# 1. Check that there have been 2 arguments sent to/with the script

if [ $# -ne 2 ]
then 
echo "distOneFileToNode.sh: Incorrect number of arguments!"
echo "./distOneFileToNode.sh -[File To Distribute] -[node IP to send to]"
exit 1
fi

echo "Executing file transfer to Node: $2"
echo scp $1 pi@$2:/home/pi/algo2/transferedFiles/

scp $1 pi@$2:/home/pi/algo2/transferedFiles/

exit 0



