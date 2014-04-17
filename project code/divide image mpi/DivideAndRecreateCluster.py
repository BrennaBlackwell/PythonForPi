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


comm = MPI.COMM_WORLD
rank = comm.Get_rank()


if rank == 0:
  original = Image.open("BadResearch.jpg")
  width, height = original.size
  oneThird = width / 3
  first = 0 + oneThird
  second = first + oneThird

  firstThird = original.crop((0, 0, first, height))
  comm.Send(firstThird, dest = 1)

  # secondThird = original.crop((first, 0, second, height))
  # comm.Send(secondThird, dest = 2)
  #
  # thirdThird = original.crop((second, 0, width, height))
  # comm.Send(thirdThird, dest = 3)

elif rank == 1:
  comm.Recv(firstThird, source = 0)
  firstThirdFilter = firstThird.filter(ImageFilter.BLUR)
  comm.Send(firstThirdFilter, dest = 0)

# elif rank == 2:
#   secondThirdFilter = secondThird.filter(ImageFilter.EMBOSS)
#   comm.Send(secondThirdFilter, dest = 0)
#
# elif rank == 3:
#   thirdThirdFilter = thirdThird.filter(ImageFilter.EDGE_ENHANCE)
#   comm.Send(thirdThirdFilter, dest = 0)

if rank == 0:
  comm.Recv(firstThirdFilter, source = 1)
  firstThirdFilter.save("FirstThirdFilter.jpg")
  # finalImage = Image.new("RGB", (width, height))
  # finalImage.paste(firstThirdFilter, (0, 0))
  # finalImage.paste(secondThirdFilter, (first, 0))
  # finalImage.paste(thirdThirdFilter, (second, 0))
  # finalImage.save("images/ReseachResult.jpg")
