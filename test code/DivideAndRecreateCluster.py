# Brenna Blackwell
# DivideAndRecreate.py
# Incorporates MPI to divide the task of applying filters to the separated image pieces.
# University of Arkansas
# CSCE Capstone II - Spring 2004

import sys
from PIL import Image, ImageFilter
from mpi4py import MPI
import colorsys
from math import ceil

def main():

  comm = MPI.COMM_WORLD
  rank = comm.Get_rank()

  if rank == 0:
    try:
      original = Image.open("images/TestImage.jpg")
    except:
        print "Unable to open image"

    try:
      width, height = original.size
      oneThird = width / 3
      first = 0 + oneThird
      second = first + oneThird

      firstThird = original.crop((0, 0, first, height))
      firstThird.save("images/FirstThird.jpg")

      secondThird = original.crop((first, 0, second, height))
      secondThird.save("images/SecondThird.jpg")

      thirdThird = original.crop((second, 0, width, height))
      thirdThird.save("images/ThirdThird.jpg")

    except:
        print "Unable to divide image"


    else if rank == 1:
      


if __name__ == '__main__':
  main()
