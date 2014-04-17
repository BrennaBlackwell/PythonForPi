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

if rank == 0:
  original = Image.open("BadResearch.jpg")
  width, height = original.size
  oneThird = width / 3
  first = 0 + oneThird
  second = first + oneThird

  firstThird = original.crop((0, 0, first, height))
  imageData = {
		'pixels':firstThird.tobytes(),
		'size':firstThird.size(), 
		'mode':firstThird.mode()
	      }
  data = pickle.dump(imageData, open("save.p", "w"))
  comm.send(data, dest = 1)

if rank == 1:
  data = comm.recv(source = 0)
  #imageData = data.get('imageData')
  #firstThird = Image.frombytes(**imageDate)
  #firstThirdFilter = firstThird.filter(ImageFilter.BLUR)
  #firstThirdFilter.save("FirstThirdFilter.jpg")
