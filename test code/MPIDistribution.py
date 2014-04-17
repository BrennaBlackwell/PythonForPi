# Brenna Blackwell
# MPIDistribution.py
# University of Arkansas
# CSCE Capstone II - Spring 2004

import sys
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
	data = {'a':5, 'b':2.5}
	comm.send(data, dest = 1)

if rank == 1:
	data = comm.recv(source = 0)
	print data.get('a')
