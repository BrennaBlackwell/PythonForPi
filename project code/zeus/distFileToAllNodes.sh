#!/bin/bash 

######### TO DO ##########################
#1. Make sure that each node has /home/pi/algo2/transferedFiles/ directory!
#############################################################
# Aurthor Nicolas Edwards
#Script takes in: 
#
#arg1=filename to be sent to all nodes
#This file will be ran by head node to distribute code to 
#the node computers.
#
#File will be placed in /home/pi/algo2/transferedFiles/ for use by the node later
#################################################################################

# 1. Check that there have been 1 arguments sent to/with the script

if [ $# -ne 1 ]
then 
echo "distFileToNodes.sh: Incorrect number of arguments!"
echo "./distFileToAllNodes.sh -[File To Distribute]"
exit 1
fi

#Head node is not included in the transfer
scp $1 pi@192.168.0.102:/home/pi/algo2/transferedFiles/
scp $1 pi@192.168.0.103:/home/pi/algo2/transferedFiles/
scp $1 pi@192.168.0.104:/home/pi/algo2/transferedFiles/

exit 0
