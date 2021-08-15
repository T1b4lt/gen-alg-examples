import random

from utils.utils import Indv


def general_crossover(selected_parents, type_genalg):
	offsprings = []
	crossover_point = random.randint(1, len(selected_parents[0]) - 2)
	if type_genalg == 1:
		for parent1 in selected_parents:
			for parent2 in selected_parents:
				if parent1 != parent2:
					offspring = Indv(6)
					offspring.weights[:crossover_point] = parent1.weights[:crossover_point]
					offspring.weights[crossover_point:] = parent2.weights[crossover_point:]
					offsprings.append(offspring)
	elif type_genalg == 2:
		for i in range(int(len(selected_parents) / 2)):
			parent1 = selected_parents[2 * i]
			parent2 = selected_parents[2 * i + 1]
			offspring = Indv(6)
			offspring.weights[:crossover_point] = parent1.weights[:crossover_point]
			offspring.weights[crossover_point:] = parent2.weights[crossover_point:]
			offsprings.append(offspring)

	print("Generated offsprings:")
	print(offsprings)
	return offsprings
