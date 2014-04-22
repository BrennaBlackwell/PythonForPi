#!/bin/bash
########## TO DO #########################
#2. ***** was seting up a global count so that images on the last pass would be output
####################################################################
#Author: Nicolas Edwards
#
#arg1: Max size of job in bytes
#
#This file will take in a directory (arg1) where there is a group of files and will 
#use another passed in value(arg2) to group the files into sub groups
#
##################################################################################

if [ $# -ne 1 ]
then
echo "distJobToNode.sh: Incorrect number of arguments"
echo "./distJobToNode.sh [Max job size in bytes]"
exit 1
fi
######### Variables ##########################
joblocation="/home/pi/algo2/Jobs/"
imageDir="/home/pi/images/"
jobname="job_"
declare -i jobnumber
jobnumber=4
declare -i jobsize
jobsize=0
#joblsit will hold string of file names to go into a job
joblist=""
declare -i filesize
declare -i numFileInDir
declare -i numFileCounted
######## Logic #########################
numFileInDir=$(ls -1 $imageDir | wc -l)
numFileCounted=0
echo "Number of files to proccess into Jobs: $numFileInDir"

cp /home/pi/algo2/job /home/pi/algo2/Jobs/job_1
cp /home/pi/algo2/job /home/pi/algo2/Jobs/job_2
cp /home/pi/algo2/job /home/pi/algo2/Jobs/job_3


for file in $imageDir*
do
filesize=$(stat -c '%s' $file)

#first check if filesize is so big it needs its own job
#next see if by adding it to joblist it will make the job to big
#if it will make the job to big then we wrap up the current joblist and send it to file
#then start a new one
#if adding the file does not make it go over the max jobsize then add it to the joblist and move to the next file

if [ $filesize -ge $1 ]; then
#goes this way if file is to big to put in a job with any other files

echo "Job Created(single file greater than max job): "$jobname$jobnumber
echo $file > $joblocation$jobname$jobnumber;

jobnumber=$jobnumber+1
numFileCounted=$numFileCounted+1
elif [ `expr $filesize + $jobsize` -gt $1 ]; then
# job is done being created
# wrap up this job and start the next one

# multi file job may not have multiple files in it
# if max job size is set low relative to image size
echo "Job Created(multi file): "$jobname$jobnumber

echo -e $joblist > $joblocation$jobname$jobnumber;

joblist=$file
jobsize=$filesize;

jobnumber=$jobnumber+1
numFileCounted=$numFileCounted+1
else
#add file to job and move on to next file check

if [ -z "$joblist" ]; then
joblist=$file
jobsize=$jobsize+$filesize
else
jobsize=$jobsize+$filesize
joblist=$joblist' '$file
fi
numFileCounted=$numFileCounted+1
fi
done

#wraps up last job
#if [ $joblist != "" ]; then
if [[ -z "$joblist" ]]; then
echo "Last job created: $joblocation$jobname$jobnumber"
echo -e $joblist > $joblocation$jobname$jobnumber;
fi
