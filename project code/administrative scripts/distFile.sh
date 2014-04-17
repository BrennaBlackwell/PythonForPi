
#copy from host to node using command line argument specified at runtime
#scp $1 pi@192.168.0.102:$1

#copy from host to node using command line argument BUT
#file is sent to specific constant location
scp $1 pi@192.168.0.102:/home/pi/algo2/transferedFiles/
scp $1 pi@192.168.0.103:/home/pi/algo2/transferedFiles/
scp $1 pi@192.168.0.104:/home/pi/algo2/transferedFiles/







