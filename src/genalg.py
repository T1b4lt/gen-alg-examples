import argparse
import random

import numpy as np

from utils.crossover import general_crossover
from utils.darwin import select_offsprings
from utils.migrations import migrate_indvs
from utils.mutation import general_mutation
from utils.utils import Population, BColors, fitness_population, select_parents, fitness_offsprings

SXIII = 1
SXXI = 2


def main(cliargs):
	print("Welcome to gen-alg-examples by T1b4lt.")

	# Typing the weights of the function to optimize #
	print("\nPlease, type the 6 weights for the equation you want to maximize")
	w1 = int(input("Weight 1: "))
	w2 = int(input("Weight 2: "))
	w3 = int(input("Weight 3: "))
	w4 = int(input("Weight 4: "))
	w5 = int(input("Weight 5: "))
	w6 = int(input("Weight 6: "))
	weights = [w1, w2, w3, w4, w5, w6]
	print(f"{BColors.OKBLUE}Weights to optimize:", weights, f"{BColors.ENDC}")

	# Select the mode of execution of the genetic algorithm #
	print("\nNow select the genetic mode of execution")
	type_genalg = int(input("Type 1 for s.XIII mode, 2 for s.XXI mode, see the differences in the README: "))
	if type_genalg == SXIII:
		print(f"{BColors.OKBLUE}You select s.XIII mode{BColors.ENDC}")
	elif type_genalg == SXXI:
		print(f"{BColors.OKBLUE}You select s.XXI mode{BColors.ENDC}")
	else:
		while True:
			type_genalg = int(input(f"{BColors.FAIL}Please, enter 1 for s.XIII mode, 2 for s.XXI mode: {BColors.ENDC}"))
			if type_genalg == SXIII:
				print(f"{BColors.OKBLUE}You select s.XIII mode{BColors.ENDC}")
				break
			elif type_genalg == SXXI:
				print(f"{BColors.OKBLUE}You select s.XXI mode{BColors.ENDC}")
				break

	# Migration #
	print("\nDo you want multiple populations and activate migration?")
	migration_input = input("Yes or No: ")
	if migration_input == "Yes":
		print(f"{BColors.OKBLUE}You select yes for migration{BColors.ENDC}")
		migration = True
	elif migration_input == "No":
		print(f"{BColors.OKBLUE}You select no for migration{BColors.ENDC}")
		migration = False
	else:
		while True:
			migration_input = input(f"{BColors.FAIL}Please, type Yes or No: {BColors.ENDC}")
			if migration_input == "Yes":
				print(f"{BColors.OKBLUE}You select yes for migration{BColors.ENDC}")
				migration = True
				break
			elif migration_input == "No":
				print(f"{BColors.OKBLUE}You select no for migration{BColors.ENDC}")
				migration = False
				break

	# Genetic algorithm variables depending of the mode #
	pop_size = 8
	num_pops = 1
	epochs = 5
	mutation_rate = -1
	darwin = False
	migration_rate = -1
	mutation_type = 1
	if type_genalg == SXIII:
		mutation_rate = 0.1
		darwin = True
		migration_rate = 0.1
	elif type_genalg == SXXI:
		mutation_rate = 0.8
		darwin = False
		migration_rate = 0.5

	if migration:
		num_pops = random.randint(2, 5)
		print("Random number of populations:", num_pops)

	# Printing final parameters of execution #
	print("\n\nFinal parameters:")
	print("Weights to optimize:", weights)
	if type_genalg == SXIII:
		print("\ttype_genalg: s.XIII")
	elif type_genalg == SXXI:
		print("\ttype_genalg: s.XXI")
	print("\tnum_pops:", num_pops)
	print("\tpop_size:", pop_size)
	print("\tepochs:", epochs)
	print("\tmutation_rate:", mutation_rate)
	print("\tdarwin:", darwin)
	print("\tmigration:", migration)
	if migration:
		print("\t\tmigration_rate:", migration_rate)

	# Init populations #
	print("\n\nInit population/s")
	populations = []
	for pop_idx in range(num_pops):
		population = Population(pop_size, indv_size=6)
		populations.append(population)
		print("Adding population to populations:\n", population)
	print("\n")
	print("Populations")
	print(populations)

	# EPOCHS #
	for epoch in range(epochs):
		print("\nEpoch", epoch + 1, "of", epochs)
		# LOOP START #
		for idx, population in enumerate(populations):
			print("\nPopulation", idx+1, "of", len(populations))
			fitness_values = fitness_population(population, weights)  # Calculate the fitness of the actual population
			selected_parents = select_parents(population, fitness_values)  # Select 50% of best parents
			offsprings_array = general_crossover(selected_parents, type_genalg)  # Cross parents to generate offsprings
			mutated_offsprings = general_mutation(offsprings_array, mutation_rate, mutation_type)  # Mutate offsprings
			if darwin:  # If darwin is True we select only population/2 offsprings for the next population
				offsprings_fitness_values = fitness_offsprings(mutated_offsprings,
															   weights)  # Calculate the fitness of the offsprings
				selected_offsprings = select_offsprings(mutated_offsprings, offsprings_fitness_values, num=int(
					len(population) / 2))  # Select the best offsprings for next generation
			else:  # If darwin is False all offsprings go to the next generation
				selected_offsprings = mutated_offsprings
			population.population = selected_parents + selected_offsprings  # Create the next generation
			populations[idx] = population  # Replace the population
			print("Max fitness of epoch:")
			max_fitness_value_epoch = 0
			for pop in populations:
				fitness_values = fitness_population(pop, weights)
				max_aux = np.max(fitness_values)
				if max_aux > max_fitness_value_epoch:
					max_fitness_value_epoch = max_aux
			print(f"{BColors.WARNING}", max_fitness_value_epoch, f"{BColors.ENDC}")
		if migration:  # If migration is True execute the method migrate_indvs
			populations = migrate_indvs(populations, migration_rate)  # Migrate indvs inter populations


if __name__ == '__main__':
	parser = argparse.ArgumentParser(
		description="genetic algorithm examples",
		epilog="A bunch of examples and possibilities to learn how genetic algorithms works.")

	args = parser.parse_args()
	main(args)
