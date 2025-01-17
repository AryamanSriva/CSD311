import random

chromosomes = {
    'X1': [6, 5, 4, 1, 3, 5, 3, 2],
    'X2': [8, 7, 1, 2, 6, 6, 0, 1],
    'X3': [2, 3, 9, 2, 1, 2, 8, 5],
    'X4': [4, 1, 8, 5, 2, 0, 9, 4]
}

def evaluate_fitness(chromosome):
    p, q, r, s, t, u, v, w = chromosome
    return (p + q) - (r + s) + (t + u) - (v + w)

fitness_scores = {key: evaluate_fitness(value) for key, value in chromosomes.items()}

sorted_chromosomes = sorted(fitness_scores.items(), key=lambda item: item[1], reverse=True)

print("Sorted chromosomes by fitness:")
for chrom, fitness in sorted_chromosomes:
    print(f"{chrom}: {chromosomes[chrom]} with fitness {fitness}")

def crossover_one_point(parent1, parent2, crossover_point):
    return parent1[:crossover_point] + parent2[crossover_point:], parent2[:crossover_point] + parent1[crossover_point:]

def crossover_two_points(parent1, parent2, crossover_point1, crossover_point2):
    return parent1[:crossover_point1] + parent2[crossover_point1:crossover_point2] + parent1[crossover_point2:], parent2[:crossover_point1] + parent1[crossover_point1:crossover_point2] + parent2[crossover_point2:]

best_chromosome = chromosomes[sorted_chromosomes[0][0]]
second_best_chromosome = chromosomes[sorted_chromosomes[1][0]]

offspring1, offspring2 = crossover_one_point(best_chromosome, second_best_chromosome, 4)
print("\nOne-Point Crossover (Middle point):")
print(f"Offspring1: {offspring1}")
print(f"Offspring2: {offspring2}")

second_fittest_chromosome = chromosomes[sorted_chromosomes[1][0]]
third_fittest_chromosome = chromosomes[sorted_chromosomes[2][0]]

offspring3, offspring4 = crossover_two_points(second_fittest_chromosome, third_fittest_chromosome, 2, 6)
print("\nTwo-Point Crossover (Between positions 2 and 6):")
print(f"Offspring3: {offspring3}")
print(f"Offspring4: {offspring4}")