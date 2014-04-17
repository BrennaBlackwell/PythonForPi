#!/bin/bash 

#######################################
#
#Create initial directories that the cluster nodes will need
#
#
#
#
#######################################
#
#
#
#
############################################



#example
#ssh pi@192.168.0.102 'rm -rf /home/pi/images; mkdir /home/pi/images

ssh pi@192.168.0.102 'rm -rf /home/pi/algo2; mkdir /home/pi/algo2; mkdir /home/pi/algo2/Jobs; mkdir /home/pi/algo2/Manip; mkdir /home/pi/algo2/Results' 
ssh pi@192.168.0.103 'rm -rf /home/pi/algo2; mkdir /home/pi/algo2; mkdir /home/pi/algo2/Jobs; mkdir /home/pi/algo2/Manip; mkdir /home/pi/algo2/Results' 
ssh pi@192.168.0.104 'rm -rf /home/pi/algo2; mkdir /home/pi/algo2; mkdir /home/pi/algo2/Jobs; mkdir /home/pi/algo2/Manip; mkdir /home/pi/algo2/Results' 


