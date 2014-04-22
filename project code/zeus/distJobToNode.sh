#!/bin/bash 

####### TO DO ######################
#1.Test this file on cluster
#
#
#
######################################
#Author: Nicolas Edwards
#
#arg1: Filename of file that contains list of files to send to node
#arg2: IP address of node to send files to
#
#Filelist that is passed in as arg1 cannot have extra newlines at the EOF
#
#Files are transfferd to /home/pi/image/
#
#
######################################



if [ $# -ne 2 ]
then
echo "distJobToNode.sh: Incorrent number of arguments"
echo "./distJobToNode.sh -[filelist] -[ip address]"
exit 1
fi

#get the number of lines in the file
#number of lines should corrosponde to number of files
#filecount=$(wc -l < $1)
declare -i filecount
filecount=0

#loop through each filename and send it to 

while read p; do
filelist="$filelist $p"
filecount=$filecount+1;
done < $1 
#echo $filecount
echo "Transfering $filecount image to leaf node: $2"
#echo scp $filelist pi@$2:/home/pi/image/
scp $filelist pi@$2:/home/pi/image/
exit 0