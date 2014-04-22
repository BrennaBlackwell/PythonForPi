#!/bin/bash 

####### TO DO ######################
#1.
######################################
#Author: Nicolas Edwards
#
#Will download result from images folder from each pi
#to Results folder of head node pi.
#
#arg1: No arguments needed. 
#
######################################

scp -r pi@192.168.0.102:/home/pi/algo2/Results /home/pi/algo2/ &
scp -r pi@192.168.0.103:/home/pi/algo2/Results /home/pi/algo2/ &
scp -r pi@192.168.0.104:/home/pi/algo2/Results /home/pi/algo2/ &

#scp -r pi@192.168.0.102:/home/pi/algo2/Results /home/pi/algo2/ &
#scp -r pi@192.168.0.103:/home/pi/algo2/Results /home/pi/algo2/ &
#scp -r pi@192.168.0.104:/home/pi/algo2/Results /home/pi/algo2/ &

#echo scp -r pi@192.168.0.102:/home/pi/algo2/Results /home/pi/algo2/ &
#echo scp -r pi@192.168.0.103:/home/pi/algo2/Results /home/pi/algo2/ &
#echo scp -r pi@192.168.0.104:/home/pi/algo2/Results /home/pi/algo2/ &



wait

