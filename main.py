from ypstruct import structure
import matplotlib.pyplot as plt
import numpy as np

import gaCrossOver
import deAlgo


pop_size = 100 #np
crossover_rate = 0.9 #cr
dimensions=[2,10,20]


#GA
# Run the genetic algorithm for each benchmark fucntions
for bm in range(1,9):
  # Run the genetic algorithm for each problem dimension
  for dim in dimensions:
      gaCrossOver.ga_logic(dim,bm)
    
     
#DE
# Run the DE for each benchmark fucntions
for i in range(1,9):
  # Run the DE for each problem dimension
  for dimIndex in range(len(dimensions)):
    problem_dimension=dimensions[dimIndex]
    deAlgo.de_logic(problem_dimension,i) #de plot are part of the DE logic implementation

