from ypstruct import structure
import matplotlib.pyplot as plt
import numpy as np
import time

import gaCrossOver
import deAlgo

pop_size = 100 #np
crossover_rate = 0.9 #cr
dimensions=[2,10,20]

#DE
# Run the DE for each benchmark fucntions
for i in range(1,9):
  process_start =None
  process_end=None
  # Run the DE for each problem dimension
  for dim in dimensions:
    process_start=time.perf_counter()
    deAlgo.de_logic(dim,i) #de plot are part of the DE logic implementation
    process_end=time.perf_counter()
    print("DE Tot Time for Dimension : "+str(dim)+" is : "+str(process_end-process_start))
    
#GA
# Run the genetic algorithm for each benchmark fucntions
for bm in range(1,9):
  process_start =None
  process_end=None
  # Run the genetic algorithm for each problem dimension
  for dim in dimensions:
      process_start=time.perf_counter()
      gaCrossOver.ga_logic(dim,bm)
      process_end=time.perf_counter()
      print("GA Tot Time for Dimension : "+str(dim)+" is : "+str(process_end-process_start))

    
    
