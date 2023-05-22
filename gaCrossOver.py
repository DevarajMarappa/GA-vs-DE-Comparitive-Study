import random
from ypstruct import structure
import matplotlib.pyplot as plt
import numpy as np
import benchmarkFunctions

#params for GA
pop_size = 100 #np
crossover_rate = 0.9 #cr
mutation_rate = 0.01 #pm
number_of_runs = 31
max_nfc = None  # Will be set based on problem dimension
prblm_dim = None  #  Will be set based on problem dimension

# population initialization
def initialize_population(pop_size, prblm_dim):
    population = []
    for _ in range(pop_size):
        individual = [random.uniform(-10,10) for _ in range(prblm_dim)]
        population.append(individual)
    return population

# single-point crossover function
def crossoverGA(parent1, parent2):
    if random.random() < crossover_rate:
        random_split = random.randint(1, len(parent1) - 1)
        child1 = parent1[:random_split] + parent2[random_split:]
        child2 = parent2[:random_split] + parent1[random_split:]
        return child1, child2
    else:
        return parent1, parent2
   
  
# Function to perform mutation
def mutation(individual):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = random.uniform(-10, 10)

# Main algorithm loop
def ga_logic(problem_dimension,bmFunc):
    global prblm_dim, max_nfc
     # Best Cost of Iterations
    #bestcost = np.empty(number_of_runs)
    fitness_values = []
    prblm_dim = problem_dimension
    max_nfc = 3000 * problem_dimension

#Execute for all bench mark functions- loop
    for run in range(number_of_runs):
        population = initialize_population(pop_size, prblm_dim)

        nfc = 0  # Number of fitness evaluations
        
        while nfc < max_nfc:
            evaluated_population = [(individual, benchmarkFunctions.evaluate_functions(bmFunc,individual)) for individual in population]
            # To get the current function name for plot purpose
            _,current_func_name=benchmarkFunctions.evaluate_functions(bmFunc,None)
            evaluated_population.sort(key=lambda x:x[1], reverse=True)
            population = [individual for individual, _ in evaluated_population]
            # Crossover and mutation
            new_population = []
            for i in range(0, pop_size, 2):
                parent1 = population[i]
                parent2 = population[i + 1] if i + 1 < pop_size else population[0]
                child1, child2 = crossoverGA(parent1, parent2)
                mutation(child1)
                mutation(child2)
                new_population.extend([child1, child2])
                nfc += 2  # Increment the fitness evaluation counter
                if nfc >= max_nfc:
                    break
            population = new_population

        best_solution = evaluated_population[0][0]
        best_fitness = evaluated_population[0][1]
        fitness_values.append(evaluated_population[0][1][0])
    print(f"Run {run + 1}: Best Solution: {best_solution}, Best Fitness: {best_fitness}")
    print("mean is : "+str( np.mean(best_solution)))
    print("std is : "+str( np.std(best_solution)))
    print("var is : "+str( np.var(best_solution)))
    generations = range(1, number_of_runs + 1)
    # Plot the best fitness value over generations
    plt.plot(generations, fitness_values)
    plt.xlabel('Generation')
    plt.ylabel('Best Fitness')
    plt.title('GA : '+current_func_name + ' , Dimension : '+str(problem_dimension))
    plt.grid(True)
    plt.savefig("plots//GA_"+current_func_name+"_"+str(problem_dimension)+"_plot.png")
    #plt.show()
    plt.clf()


