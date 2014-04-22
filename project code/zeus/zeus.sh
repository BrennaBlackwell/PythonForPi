#!/bin/bash 
####### TO DO ######################
#
######################################
# Author: Nicolas Edwards
#
# It is assumed that you will be running zeus.sh
# in the same directory with all the other script files
# and with the same directory structure as noted in the
# documentation. 
######################################
echo ""
echo ""

echo "Zeus command start of prepareCluster.sh ..."
./prepareCluster.sh
echo "Zeus command complete: prepareCluster.sh"
echo ""
echo ""

echo "Zeus command start of groupJobs.sh ..."
#arg1 is the max job size to allow in bytes
./groupJobs.sh 120000
echo "Zeus command complete: groupJobs.sh"
echo ""
echo ""

echo "Zeus command start of nodeExecute.sh ..."
ssh pi@192.168.0.102 'cd /home/pi/algo2/; ./nodeExecute.sh 102' & 
ssh pi@192.168.0.103 'cd /home/pi/algo2/; ./nodeExecute.sh 103' & 
ssh pi@192.168.0.104 'cd /home/pi/algo2/; ./nodeExecute.sh 104' & 
echo "Zeus command complete: nodeExecute.sh"
echo ""
echo ""

echo "Zeus command start of launchJobs.sh ..."
./launchJobs.sh
wait
echo "Zeus command complete: launchJobs.sh"
echo ""
echo ""

echo "Zeus command start of getResults.sh ..."
./getResults.sh
echo "Zeus command complete: getResults.sh"
echo ""
echo ""
echo "Zeus algorithm done. Results are in results folder."
