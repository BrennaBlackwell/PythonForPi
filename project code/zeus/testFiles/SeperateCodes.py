#SeperateCodes.py
from mpi4py import MPI
import sys

size = MPI.COMM_WORLD.Get_size()
rank = MPI.COMM_WORLD.Get_rank()
name = MPI.Get_processor_name()


#a = 6.0
#b = 3.0

if rank == 0:
	#print a + b
	sys.stdout.write("Process %d of %d on %s.\n\n" % (rank, size, name))
	
elif rank == 1:
	#print a * b
	sys.stdout.write("Process %d of %d on %s.\n\n" % (rank, size, name))

elif rank == 2:
	#print a - b
	sys.stdout.write("Process %d of %d on %s.\n\n" % (rank, size, name))

elif rank == 3:
	#print b - a
	sys.stdout.write("Process %d of %d on %s.\n\n" % (rank, size, name))

else:
	#print "Rank is greater than 3"
	sys.stdout.write("Process %d of %d on %s.\n\n" % (rank, size, name))