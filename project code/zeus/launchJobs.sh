#!/bin/bash 
####### TO DO ######################
# 1.Each node will write 102, 103, 104 to specify the last number of ip
# when that node needs another job. 
######################################
# Author: Nicolas Edwards
#
######################################
############# VARIBLES ###############
jobLocation="/home/pi/algo2/Jobs/"
msgLocation="/home/pi/algo2/Mesgs/msgs.txt"
jobName="job_"
declare -i numOfMesgs
numOfMesgs=0
declare -i jobsLeftCount
jobsLeftCount=$(ls -1 $jobLocation | wc -l)
declare -i msgLines
declare -i endMsgCount=0
declare -i temp
################ LOGIC ################
echo "Starting job count for head node is: $jobsLeftCount"
#send out first 3 jobs to pis
mv $jobLocation$jobName$jobsLeftCount /home/pi/algo2/Jobs/job
jobsLeftCount=$jobsLeftCount-1;
scp /home/pi/algo2/Jobs/job pi@192.168.0.102:/home/pi/algo2/Jobs/
mv $jobLocation$jobName$jobsLeftCount /home/pi/algo2/Jobs/job
jobsLeftCount=$jobsLeftCount-1;
scp /home/pi/algo2/Jobs/job pi@192.168.0.103:/home/pi/algo2/Jobs/
mv $jobLocation$jobName$jobsLeftCount /home/pi/algo2/Jobs/job
jobsLeftCount=$jobsLeftCount-1;
scp /home/pi/algo2/Jobs/job pi@192.168.0.104:/home/pi/algo2/Jobs/
echo "Head node has $jobsLeftCount remaining "

# Now go into loop to send out jobs as pis ask for more work
#---------------------- while loop begin----------------------------------
while [ $jobsLeftCount -gt 0 ]
do
msgLines=$(wc -l < $msgLocation)
if [ $msgLines ]; then
#FIND WAY TO LOCK FILE AND DO THAT HERE
#echo "launchJobs.sh: Messages found. Locking message file to read contents"
endMsgCount=$msgLines
{
flock -e 350
while read line; do 
 
if [ $jobsLeftCount -gt 0 ]; then
echo "Message Received from: $line     : Sending job $jobsLeftCount"
#rename file to be sent to node "job"
mv $jobLocation$jobName$jobsLeftCount /home/pi/algo2/Jobs/job
#transfer new job to each script that left a message
scp /home/pi/algo2/Jobs/job pi@192.168.0.$line:/home/pi/algo2/Jobs/
jobsLeftCount=$jobsLeftCount-1;
endMsgCount=$endMsgCount-1
fi
done < $msgLocation;

#clear msg file
>$msgLocation;
#UNLOCK MESG FILE HERE
} 350>>$msgLocation
fi
done
#----------------end while loop ------------

#all jobs are done being handed out but now
#we must wait for all jobs to finish completing
# Have to lock file before I access it. 


#temp=$endMsgCount
#while [ $temp -ne 3 ]
#do
#echo "waiting on my children"
#msgLines=$(wc -l < $msgLocation)
#temp=$msgLines+$endMsgCount
#done

#send dummy job to nodes with "killShell" as the only line
#scp /home/pi/algo2/job pi@192.168.0.102:/home/pi/algo2/Jobs/
#scp /home/pi/algo2/job pi@192.168.0.103:/home/pi/algo2/Jobs/
#scp /home/pi/algo2/job pi@192.168.0.104:/home/pi/algo2/Jobs/

exit 0