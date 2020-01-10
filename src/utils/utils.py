import uuid

import numpy as np


class BColors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'


class Indv:
	def __init__(self, indv_size):
		self.indv_size = indv_size
		self.weights = np.random.uniform(-4.0, 4.0, indv_size)
		self.uuid = uuid.uuid4()

	def __str__(self):
		return 'Indv weights: {self.weights} uuid: {self.uuid}'.format(self=self)

	def __repr__(self):
		return self.weights.__str__()

	def __len__(self):
		return self.indv_size


class Population:
	def __init__(self, pop_size, indv_size):
		self.population = []
		self.pop_size = pop_size
		self.indv_size = indv_size
		self.uuid = uuid.uuid4()
		for indv_idx in range(self.pop_size):
			self.population.append(Indv(indv_size))

	def __str__(self):
		return 'Population of {self.pop_size} indviduals with uuid: {self.uuid}\n{self.population}'.format(self=self)

	def __repr__(self):
		return self.population.__str__()

	def __len__(self):
		return len(self.population)


def fitness_offsprings(mutated_offsprings, func_weights):
	fitness_array = []
	for indv in mutated_offsprings:
		fitness_array.append(fitness_max_function(indv.weights, func_weights))
	print("Actual offsprings fitness values:")
	print(fitness_array)
	return fitness_array


def fitness_population(population, func_weights):
	fitness_array = []
	for indv in population.population:
		fitness_array.append(fitness_max_function(indv.weights,
												  func_weights))  # Calculate the fitness value for each indv of the population
	print("Actual fitness values:")
	print(fitness_array)
	return fitness_array


def fitness_max_function(indv_weights, func_weights):
	return np.dot(indv_weights, func_weights)


def select_parents(population, fitness_values):
	num_parents = int(len(population) / 2)  # We want the best 50% of the parents
	parents = []
	for parent_num in range(num_parents):  # For each parent
		max_fitness_idx = np.where(fitness_values == np.max(fitness_values))  # Get the index of the max fitness value
		max_fitness_idx = max_fitness_idx[0][0]
		parents.append(population.population[max_fitness_idx])
		fitness_values[max_fitness_idx] = -99999999999  # Change his fitness to a minimum
	print("Selected parents:")
	print(parents)
	return parents
