#!/bin/bash 
FILES=/home/pi/images/*
for f in $FILES
do
  echo "Processing $f file..."
  echo $(basename $f)
  # take action on each file. $f store current file name
done