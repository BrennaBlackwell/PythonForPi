# Brenna Blackwell
# DivideAndRecreateCluster.py
# Incorporates MPI to divide the task of applying filters to the separated image pieces.
# University of Arkansas
# CSCE Capstone II - Spring 2004

import sys
from PIL import Image, ImageFilter
from mpi4py import MPI
import colorsys
from math import ceil
import pickle

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
name = MPI.Get_processor_name()
#size = MPI.COMM_WORLD.Get_size()
#sys.stdout.write("Process %d of %d on %s.\n" % (rank, size, name))

if rank == 0:
  #Open original image and calculate the division of it
  original = Image.open("BadResearch.jpg")
  width, height = original.size
  oneThird = width / 3
  first = 0 + oneThird
  second = first + oneThird

  #Remove the first third and send it to Process Rank 1
  firstThird = original.crop((0, 0, first, height))
  firstThirdImageData = {
		'pixels':firstThird.tobytes(),
		'size':firstThird.size,
		'mode':firstThird.mode,
	      }
  firstThirdToSend = {'image':firstThirdImageData}
  comm.send(firstThirdToSend, dest = 1)

  #Remove the second third and send it to Process Rank 2
  secondThird = original.crop((first, 0, second, height))
  secondThirdImageData = {
    'pixels':secondThird.tobytes(),
    'size':secondThird.size,
    'mode':secondThird.mode,
        }
  secondThirdToSend = {'image':secondThirdImageData}
  comm.send(secondThirdToSend, dest = 2)

  #Remove the third third and send it to Process Rank 3
  thirdThird = original.crop((second, 0, width, height))
  thirdThirdImageData = {
    'pixels':thirdThird.tobytes(),
    'size':thirdThird.size,
    'mode':thirdThird.mode,
        }
  thirdThirdToSend = {'image':thirdThirdImageData}
  comm.send(thirdThirdToSend, dest = 3)

  #Receive filtered image portions back from leaf nodes
  firstFilterData = comm.recv(source = 1)
  firstFilter = firstFilterData.get('image')
  firstFilterPixels = firstFilter.get('pixels')
  firstFilterSize = firstFilter.get('size')
  firstFilterMode = firstFilter.get('mode')
  firstThirdFilter = Image.frombytes(firstFilterMode, firstFilterSize, firstFilterPixels)

  secondFilterData = comm.recv(source = 2)
  secondFilter = secondFilterData.get('image')
  secondFilterPixels = secondFilter.get('pixels')
  secondFilterSize = secondFilter.get('size')
  secondFilterMode = secondFilter.get('mode')
  secondThirdFilter = Image.frombytes(secondFilterMode, secondFilterSize, secondFilterPixels)

  thirdFilterData = comm.recv(source = 3)
  thirdFilter = thirdFilterData.get('image')
  thirdFilterPixels = thirdFilter.get('pixels')
  thirdFilterSize = thirdFilter.get('size')
  thirdFilterMode = thirdFilter.get('mode')
  thirdThirdFilter = Image.frombytes(thirdFilterMode, thirdFilterSize, thirdFilterPixels)

  #Reassemble and save altered image
  finalImage = Image.new("RGB", (width, height))
  finalImage.paste(firstThirdFilter, (0, 0))
  finalImage.paste(secondThirdFilter, (first, 0))
  finalImage.paste(thirdThirdFilter, (second, 0))
  finalImage.save("FinalBadResearch.jpg")

if rank == 1:
  #Receive image portion from head node
  data = comm.recv(source = 0)
  receivedImageData = data.get('image')
  receivedImagePixels = receivedImageData.get('pixels')
  receivedImageSize = receivedImageData.get('size')
  receivedImageMode = receivedImageData.get('mode')
  receivedImage = Image.frombytes(receivedImageMode, receivedImageSize, receivedImagePixels)
  firstThirdFilter = receivedImage.filter(ImageFilter.BLUR)

  #Send filtered image back to head node
  firstThirdFilterImageData = {
    'pixels':firstThirdFilter.tobytes(),
    'size':firstThirdFilter.size,
    'mode':firstThirdFilter.mode,
    }
  firstThirdFilterToSend = {'image':firstThirdFilterImageData}
  comm.send(firstThirdFilterToSend, dest = 0)

if rank == 2:
  #Receive image portion from head node
  data = comm.recv(source = 0)
  receivedImageData = data.get('image')
  receivedImagePixels = receivedImageData.get('pixels')
  receivedImageSize = receivedImageData.get('size')
  receivedImageMode = receivedImageData.get('mode')
  receivedImage = Image.frombytes(receivedImageMode, receivedImageSize, receivedImagePixels)
  secondThirdFilter = receivedImage.filter(ImageFilter.EMBOSS)

  #Send filtered image back to head node
  secondThirdFilterImageData = {
    'pixels':secondThirdFilter.tobytes(),
    'size':secondThirdFilter.size,
    'mode':secondThirdFilter.mode,
    }
  secondThirdFilterToSend = {'image':secondThirdFilterImageData}
  comm.send(secondThirdFilterToSend, dest = 0)

if rank == 3:
  #Receive image portion from head node
  data = comm.recv(source = 0)
  receivedImageData = data.get('image')
  receivedImagePixels = receivedImageData.get('pixels')
  receivedImageSize = receivedImageData.get('size')
  receivedImageMode = receivedImageData.get('mode')
  receivedImage = Image.frombytes(receivedImageMode, receivedImageSize, receivedImagePixels)
  thirdThirdFilter = receivedImage.filter(ImageFilter.EDGE_ENHANCE)

  #Send filtered data back to head node
  thirdThirdFilterImageData = {
    'pixels':thirdThirdFilter.tobytes(),
    'size':thirdThirdFilter.size,
    'mode':thirdThirdFilter.mode,
    }
  thirdThirdFilterToSend = {'image':thirdThirdFilterImageData}
  comm.send(thirdThirdFilterToSend, dest = 0)
