#!/bin/bash 
####### TO DO ######################
#
######################################
#Author: Nicolas Edwards
#
# arg1: 3digit of ip address that can be used when writing message
# to msg.txt file. 
#
#
# Will begin execution after first Job has been
# placed in job folder.
######################################

#the job directory is initially empty
while [ ! -s /home/pi/algo2/Jobs/job ]
do
sleep 0
done

while [ 1 ]
do
#kill script if it has been sent killShell command
if [ "$(head -1 /home/pi/algo2/Jobs/job)" == "killShell" ]; then
echo "Node work done. Exiting node ** $1 **"
exit 0
fi 

# build job string
imageList=$(cat /home/pi/algo2/Jobs/job)
# use scp to download all the files
echo scp pi@192.168.0.101:"$imageList" /home/pi/images/
scp pi@192.168.0.101:"$imageList" /home/pi/images/

#Wrap python script call so that it is called for each of the images in the image folder


# Launch python manipulation script 
#python /home/pi/algo2/Manip/manipulation.py 
FILES=/home/pi/images/*
for f in $FILES
do
  python /home/pi/algo2/Manip/manipulation.py $(basename $f)
done




# delete job file when done with job
rm /home/pi/algo2/Jobs/job

# delete images from image dir
rm -rf /home/pi/images
mkdir /home/pi/images

# ssh into head node and add ip address to msg.txt file
# write script that takes in last 3 digits of ip address of 
# node pi and have that script reside on head node. Leaf
# nodes will ssh in and call that script with the corospoding
# argument so the script on the head node will do the locked
# addition to the msg.txt file.

ssh pi@192.168.0.101 "cd /home/pi/algo2; ./addMsg.sh $1" 

# wait for head node to send another job. If it is the killShell
# job then it will be caught at the top of the loop
while [ ! -s /home/pi/algo2/Jobs/job ]
do
# while the job directory is empty just wait
sleep 0
done

done

