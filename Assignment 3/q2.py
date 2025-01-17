def evaluate_fitness(x):
    return 15 * x - x**2

def convert_to_decimal(binary_strings):
    return [int(b, 2) for b in binary_strings]

def compute_fitness(population):
    return [evaluate_fitness(x) for x in population]

def calculate_selection_proportions(fitness_values):
    total = sum(fitness_values)
    return [(fv / total) * 100 for fv in fitness_values], total

def crossover_parents(parent1, parent2, crossover_point):
    offspring1 = parent1[:crossover_point] + parent2[crossover_point:]
    offspring2 = parent2[:crossover_point] + parent1[crossover_point:]
    return offspring1, offspring2

def mutate_binary(binary_string, mutation_positions):
    binary_list = list(binary_string)
    for pos in mutation_positions:
        binary_list[pos] = '1' if binary_list[pos] == '0' else '0'
    return ''.join(binary_list)

def display_roulette_wheel(fitness_proportions):
    print("\n--- Roulette Wheel Selection ---")
    for i, proportion in enumerate(fitness_proportions):
        print(f"Individual {i+1}: {proportion:.2f}%")

initial_population = ["1100", "0100", "0001", "1110", "0111", "1001"]

decimal_values = convert_to_decimal(initial_population)
fitness_scores = compute_fitness(decimal_values)
selection_proportions, total_fitness = calculate_selection_proportions(fitness_scores)

print("Initial Fitness Scores:", fitness_scores)
display_roulette_wheel(selection_proportions)

initial_population[5], initial_population[1] = crossover_parents(initial_population[5], initial_population[1], 3)
print("\nPopulation after Crossover:", initial_population)

initial_population[0] = mutate_binary(initial_population[0], [1, 2])  
initial_population[4] = mutate_binary(initial_population[4], [1, 2])  
print("\nPopulation after Mutation:", initial_population)

decimal_values = convert_to_decimal(initial_population)
new_fitness_scores = compute_fitness(decimal_values)
new_selection_proportions, new_total_fitness = calculate_selection_proportions(new_fitness_scores)

print("\nUpdated Fitness Scores:", new_fitness_scores)
display_roulette_wheel(new_selection_proportions)

fitness_improvement = ((new_total_fitness - total_fitness) / total_fitness) * 100
print(f"\nFitness Improvement: {fitness_improvement:.2f}%")