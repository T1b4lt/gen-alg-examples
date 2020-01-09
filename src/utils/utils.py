import uuid

import numpy as np


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


def fitness_population(population, weights):
	print("FITNESS")
	return []


def select_parents(population, fitness_values):
	print("SELECT PARENTS")
	return []
