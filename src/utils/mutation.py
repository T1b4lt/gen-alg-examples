import random

import numpy as np


def general_mutation(offsprings_array, mutation_rate, mutation_type):
	for idx in range(len(offsprings_array)):
		random_value = np.random.uniform(-1.0, 1.0, 1)
		random_idx = random.randint(0, len(offsprings_array[0]) - 1)
		offsprings_array[idx].weights[random_idx] = offsprings_array[idx].weights[random_idx] + random_value
	print("Mutated offsprings:")
	print(offsprings_array)
	return offsprings_array
