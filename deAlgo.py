import numpy as np
import matplotlib.pyplot as plt
import random

import BenchmarkFunctions


dims = [2,10,20]
number_of_runs = 31
pop_size=100
mf=0.8 #mutation factor
Cr=0.9 #crossover rate
problem_dimension=None

# Mutation
def mutation(population, target_index):
    a, b, c = random.sample(range(pop_size), 3)
    mutant = population[a] + mf * (population[b] - population[c])
    return mutant

# DE Crossover
def deCrossover(population, target_index, mutant, prblm_dim):
    target = population[target_index]
    trial = np.copy(target)
    for i in range(prblm_dim):
        if random.random() < Cr:
            trial[i] = mutant[i]
    return trial

# Initialize  population
def init_population(population_size, problem_dimension):
    population = []
    for _ in range(population_size):
        individual = np.random.uniform(-10, 10, problem_dimension)
        population.append(individual)
    return population

# Main algorithm loop
def de_logic(problem_dimension,benfunc):   
        
    population = init_population(pop_size, problem_dimension)
    best_solution = None
    best_fitness = float('-inf')
    fitness_values = []  # Store fitness values for plotting
    for generation in range(number_of_runs):
        for i in range(pop_size):
            target = population[i]
            mutant = mutation(population, i)
            trial = deCrossover(population, i, mutant, problem_dimension)
            target_fitness , func_name = BenchmarkFunctions.evaluate_functions(benfunc,target)
            trial_fitness, func_name = BenchmarkFunctions.evaluate_functions(benfunc,trial)
            if trial_fitness > target_fitness:
                population[i] = trial
                if trial_fitness > best_fitness:
                    best_solution = trial
                    best_fitness = trial_fitness
        fitness_values.append(best_fitness)
    # Plot optimization progress
    generations = range(1, number_of_runs + 1)
    plt.plot(generations, fitness_values, 'b')
    plt.xlabel('Generation')
    plt.ylabel('Fitness')
    plt.title('DE Optimization Progress : '+func_name + ' , Dimension : '+str(problem_dimension))
    plt.grid(True)
    plt.show()
    print(f"Best Solution: {best_solution}, Best Fitness: {best_fitness}")
    print(func_name)
