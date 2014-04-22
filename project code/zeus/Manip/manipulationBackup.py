#!/usr/bin/python
import glob
import shutil
import os

# My first python program
# print "Hello, World!\n"

src_dir = "/home/pi/images"
dst_dir = "/home/pi/algo2/Results"

for thisFile in glob.iglob(os.path.join(src_dir, "*")):
	shutil.copy(thisFile, dst_dir)



