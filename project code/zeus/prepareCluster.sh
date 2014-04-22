#!/bin/bash 
####### TO DO ######################
#
######################################
# Author: Nicolas Edwards
#
# Script will delete 1. Contents of Results folder on all pis
# 2. jobs on all pis. 3. manipulation.sh script.
# It will then send the new manipulation script that has been passed in as arg1
# manipulation script is assumed to be in the /home/pi/algo2/Manip/ directory
#
# file that you want distributed must be called manipulation.py
# and be in the /home/pi/algo2/Manip/ folder
#
######################################

# LOCAL ACTIONS

# Delete contents of local job directory
rm -rf /home/pi/algo2/Jobs
mkdir /home/pi/algo2/Jobs
echo "Local Jobs folder cleaned"
# Clean out Message file
rm /home/pi/algo2/Mesgs/msgs.txt
touch /home/pi/algo2/Mesgs/msgs.txt
echo "Local Message file cleaned"
# Clean out results folder
rm -rf /home/pi/algo2/Results
mkdir /home/pi/algo2/Results

echo "Local Results folder cleaned"

# NON-LOCAL ACTIONS

# Delete algo2 directory and all its contents and then
# remake the empty directory structure.
ssh pi@192.168.0.102 'rm -rf /home/pi/images; mkdir /home/pi/images; rm -rf /home/pi/algo2; mkdir /home/pi/algo2; mkdir /home/pi/algo2/Jobs; mkdir /home/pi/algo2/Manip; mkdir /home/pi/algo2/Results' 
ssh pi@192.168.0.103 'rm -rf /home/pi/images; mkdir /home/pi/images; rm -rf /home/pi/algo2; mkdir /home/pi/algo2; mkdir /home/pi/algo2/Jobs; mkdir /home/pi/algo2/Manip; mkdir /home/pi/algo2/Results' 
ssh pi@192.168.0.104 'rm -rf /home/pi/images; mkdir /home/pi/images; rm -rf /home/pi/algo2; mkdir /home/pi/algo2; mkdir /home/pi/algo2/Jobs; mkdir /home/pi/algo2/Manip; mkdir /home/pi/algo2/Results' 
echo "Node directory structures cleaned..."

# Send new image manipulation script
scp /home/pi/algo2/Manip/manipulation.py pi@192.168.0.102:/home/pi/algo2/Manip
scp /home/pi/algo2/Manip/manipulation.py pi@192.168.0.103:/home/pi/algo2/Manip
scp /home/pi/algo2/Manip/manipulation.py pi@192.168.0.104:/home/pi/algo2/Manip
echo "Python manipulation file ** manipulation.py ** uploaded to nodes..."

# Send nodeExecute.sh script to all pis
scp /home/pi/algo2/nodeExecute.sh pi@192.168.0.102:/home/pi/algo2/
scp /home/pi/algo2/nodeExecute.sh pi@192.168.0.103:/home/pi/algo2/
scp /home/pi/algo2/nodeExecute.sh pi@192.168.0.104:/home/pi/algo2/
echo "Node execution file ** nodeExecute.sh ** uploaded to nodes..."
