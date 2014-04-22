#!/bin/bash 
####### TO DO ######################
#
######################################
# Author: Nicolas Edwards
#
# arg1: 3 digts to add to msg.txt file
######################################

(
flock -e 350
echo "$1">>/home/pi/algo2/Mesgs/msgs.txt
) 350>>/home/pi/algo2/Mesgs/msgs.txt




