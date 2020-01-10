import numpy as np


def select_offsprings(mutated_offsprings, offsprings_fitness_values, num=4):
	selected_offsprings = []  # Init the selected_offsprings array to be returned
	for offspring_num in range(num):  # For each offspring
		max_fitness_idx = np.where(
			offsprings_fitness_values == np.max(offsprings_fitness_values))  # Get the index of the max fitness value
		max_fitness_idx = max_fitness_idx[0][0]
		selected_offsprings.append(mutated_offsprings[max_fitness_idx])  # Save the offspring in his position
		offsprings_fitness_values[max_fitness_idx] = -99999999999  # Change his fitness to a minimum
	print("Selected offsprings:")
	print(selected_offsprings)
	return selected_offsprings
