# Brenna Blackwell
# launch.sh
# Launches DivideAndRecreateCluster.py program
# University of Arkansas
# CSCE Capstone II - Spring 2004

{ time mpiexec -machinefile machinefile -n 4 python DivideAndRecreateCluster.py x.jpg ; } 2>> time.txt # >> result.txt
{ time mpiexec -machinefile machinefile -n 4 python DivideAndRecreateCluster.py zzzzz.jpg ; } 2>> time.txt # >> result.txt
{ time mpiexec -machinefile machinefile -n 4 python DivideAndRecreateCluster.py zzzz.jpg ; } 2>> time.txt # >> result.txt
{ time mpiexec -machinefile machinefile -n 4 python DivideAndRecreateCluster.py zzz.jpg ; } 2>> time.txt # >> result.txt
{ time mpiexec -machinefile machinefile -n 4 python DivideAndRecreateCluster.py zz.jpg ; } 2>> time.txt # >> result.txt
{ time mpiexec -machinefile machinefile -n 4 python DivideAndRecreateCluster.py z.jpg ; } 2>> time.txt # >> result.txt
{ time mpiexec -machinefile machinefile -n 4 python DivideAndRecreateCluster.py y.jpg ; } 2>> time.txt # >> result.txt
{ time mpiexec -machinefile machinefile -n 4 python DivideAndRecreateCluster.py xxx.jpg ; } 2>> time.txt # >> result.txt
{ time mpiexec -machinefile machinefile -n 4 python DivideAndRecreateCluster.py xx.jpg ; } 2>> time.txt # >> result.txt
{ time mpiexec -machinefile machinefile -n 4 python DivideAndRecreateCluster.py Weight.jpg ; } 2>> time.txt # >> result.txt
{ time mpiexec -machinefile machinefile -n 4 python DivideAndRecreateCluster.py tutscrn.jpg ; } 2>> time.txt # >> result.txt
{ time mpiexec -machinefile machinefile -n 4 python DivideAndRecreateCluster.py tecyhtime.jpg ; } 2>> time.txt # >> result.txt
{ time mpiexec -machinefile machinefile -n 4 python DivideAndRecreateCluster.py tartu_univ.jpg ; } 2>> time.txt # >> result.txt
{ time mpiexec -machinefile machinefile -n 4 python DivideAndRecreateCluster.py syntspec.jpg ; } 2>> time.txt # >> result.txt
{ time mpiexec -machinefile machinefile -n 4 python DivideAndRecreateCluster.py Comments.jpg ; } 2>> time.txt # >> result.txt