# Joshua Ross
# imgpipe.py
# using MPI, passes a series of images from the head node through the leaf
#	nodes, each leaf performing a distinct operation on the image.

import sys
import time
from mpi4py import MPI
from PIL import Image, ImageFilter, ImageOps
from Queue import *
import pickle

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
	
	#each node works as follows:
	#0 - open images, put in queue, pass first to 1
	#1 - get image, add effect, pass to 2
	#2 - get image, add effect, pass to 3
	#3 - get image, add effect, save image
	
if rank == 0:

	start_time = time.time()
	images = Queue(maxsize = 0)

	for item in sys.argv:
		if item != "imgpipe.py":
			images.put(Image.open(item))
			print "Loaded image ", item

	#images.put(Image.open("image01.jpg"))
	#images.put(Image.open("image02.jpg"))
	#images.put(Image.open("image03.jpg"))
	#images.put(Image.open("image04.jpg"))
	#images.put(Image.open("image05.jpg"))
	#images.put(Image.open("image06.jpg"))

	numImages = images.qsize()

	while images.empty() == False:
		imgNum = numImages - images.qsize() #appended to end of filename
	
		#put it in a pickle object to send
		imageS = images.get()
		imData = {
			'pixels': imageS.tobytes(),
			'size': imageS.size,
			'mode': imageS.mode,
			'imgnum': imgNum,
			'numLeft': images.qsize(),
			}
		imSend = {'image':imData}
		
		#send images
		print "About to send image %i of %i." % (imgNum, numImages)
		comm.send(imSend, dest = 1)
		print "Sent image %i of %i." % (imgNum, numImages)

	#receive collection of finished images
	print "About to receive all finished images."
	recvListData = comm.recv(source = 3)
	recvList = recvListData.get('list')
	print "Finished images received."

	for index, item in enumerate(recvList):
		r0Recv = item.get('image')
		r0RecvMode = r0Recv.get('mode')
		r0RecvSize = r0Recv.get('size')
		r0RecvPixels = r0Recv.get('pixels')
		r0Image = Image.frombytes(r0RecvMode, r0RecvSize, r0RecvPixels)
		
		filenameStr = "imageF%i.jpg" % (index)
		r0Image.save(filenameStr)

	end_time = time.time() - start_time
	time_per_image = end_time / numImages

	print "Total time: ", end_time
	print "Average time per image: ", time_per_image
		
elif rank == 1:
	while True:
		r1RecvData = comm.recv(source = 0)
		r1Recv = r1RecvData.get('image')
		r1RecvNumLeft = r1Recv.get('numLeft')
		r1RecvImgnum = r1Recv.get('imgnum')
		r1RecvMode = r1Recv.get('mode')
		r1RecvSize = r1Recv.get('size')
		r1RecvPixels = r1Recv.get('pixels')
		r1Image = Image.frombytes(r1RecvMode, r1RecvSize, r1RecvPixels)
		
		r1Image = r1Image.filter(ImageFilter.CONTOUR)
		
		r1Send = {
			'pixels': r1Image.tobytes(),
			'size': r1Image.size,
			'mode': r1Image.mode,
			'imgnum': r1RecvImgnum,
			'numLeft': r1RecvNumLeft,
			}
		r1SendData = {'image':r1Send}
		
		comm.send(r1SendData, dest = 2)

		if r1RecvNumLeft == 0:
			break

elif rank == 2:
	while True:
		r2RecvData = comm.recv(source = 1)
		r2Recv = r2RecvData.get('image')
		r2RecvNumLeft = r2Recv.get('numLeft')
		r2RecvImgnum = r2Recv.get('imgnum')
		r2RecvMode = r2Recv.get('mode')
		r2RecvSize = r2Recv.get('size')
		r2RecvPixels = r2Recv.get('pixels')
		r2Image = Image.frombytes(r2RecvMode, r2RecvSize, r2RecvPixels)
		
		r2Image = ImageOps.invert(r2Image)
		
		r2Send = {
			'pixels': r2Image.tobytes(),
			'size': r2Image.size,
			'mode': r2Image.mode,
			'imgnum': r2RecvImgnum,
			'numLeft': r2RecvNumLeft,
			}
		r2SendData = {'image':r2Send}
		
		comm.send(r2SendData, dest = 3)

		if r2RecvNumLeft == 0:
			break

else:
	final = []	#this list will be used to return all completed images
	while True:
		r3RecvData = comm.recv(source = 2)
		r3Recv = r3RecvData.get('image')
		r3RecvNumLeft = r3Recv.get('numLeft')
		r3RecvImgnum = r3Recv.get('imgnum')
		r3RecvMode = r3Recv.get('mode')
		r3RecvSize = r3Recv.get('size')
		r3RecvPixels = r3Recv.get('pixels')
		r3Image = Image.frombytes(r3RecvMode, r3RecvSize, r3RecvPixels)
		
		r3Image = ImageOps.flip(r3Image)
		
		#now to serialize each image and put the object in the list
		r3ListObj = {
			'pixels': r3Image.tobytes(),
			'size': r3Image.size,
			'mode': r3Image.mode,
			}
		r3ListObjData = {'image':r3ListObj}
		
		final.append(r3ListObjData)

		if r3RecvNumLeft == 0:
			break

	#And now serialize the list to be able to send it
	finalSendData = {'list':final}
	comm.send(finalSendData, dest = 0)
