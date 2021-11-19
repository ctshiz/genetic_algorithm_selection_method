import numpy as np
import random
import pandas as pd

#creating an individual of 5 elements from random numbers between 0 and 100
def generate_individual():
    individual = random.sample(range(0,100), 5)
    return individual

#creating the initial population of 5 individuals
def generate_population(counter):
    population = []
    for c in range(counter):
        individual = generate_individual()
        population.append(individual)
    return population

#compute the fitness of each individual in the population
def generate_fitness(population):
    #choose the fitness to be the sum of the elements in the individual to be equal to 165
    fitness_list = []
    for _ in range(len(population)):
        fitness_score = np.sum(population[_])
        fitness_list.append(fitness_score)
    return fitness_list

pop = generate_population(5)
fit_score = generate_fitness(pop)
print('the population is ', pop)
print('The fitness score is', fit_score)


#understanding the selection methods
#1.roulette wheel selection

#compute the relative portion
rel_port = []
sum_fit_score = np.sum(fit_score)

for _ in range(len(pop)):
    rel_port.append([pop[_], fit_score[_], fit_score[_] / sum_fit_score])

#define a dataframe of the relative portion
df_relative_portion = pd.DataFrame(rel_port, columns=["individual", "fitness", "relative_portion"])
#print(df_relative_portion)

#rank-based selection
def generate_rank(fit_score):
    #define a empty list to hold the rank of the fitness score
    rank = []
    #sort the fitness score list
    fit_score_order = np.sort(fit_score)
    for _ in range(len(fit_score_order)):
        rank.append([_ + 1, fit_score_order[_]])
    return rank

rank_list = generate_rank(fit_score)
print("the rank list is ", rank_list)

#sum all the rank
def generate_sum_rank(rank_list):
    sum_rank = 0
    for _ in range(len(rank_list)):
        sum_rank += rank_list[_][0]
    return sum_rank

sum_rank = generate_sum_rank(rank_list)
print("The sum of the ranks is ", sum_rank)

rank_order = []
for _ in range(len(rank_list)):
    for __ in range(len(fit_score)):
        if rank_list[_][1] == fit_score[__]:
            rank_order.append([pop[_], fit_score[_], rank_list[_][0], rank_list[_][0] / sum_rank])
        else:
            continue

#define a dataframe of the relative portion
df_rank_portion = pd.DataFrame(rank_order, columns=["individual", "fitness", "rank", "relative_portion"])

print(df_rank_portion)
