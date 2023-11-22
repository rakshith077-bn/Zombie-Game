import random
import time

class Individual:
    def __init__(self, genes):
        self.genes = genes

def generate_individual(length):
    return Individual(genes=[random.choice(['A', 'B', 'C', 'D']) for _ in range(length)])

def calculate_fitness(person):
    target_sequence = ['A', 'B', 'C', 'A']  # Replace with your target sequence
    fitness = 0

    for i in range(len(target_sequence)):
        if person.genes[i] == target_sequence[i]:
            fitness += 1

    return fitness

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1.genes) - 1)
    child_genes = parent1.genes[:crossover_point] + parent2.genes[crossover_point:]
    child = Individual(genes=child_genes)

    print(f"{parent1.genes[0]} and {parent2.genes[0]} crossed the bridge.")
    print(f"{parent2.genes[0]} returned with the lantern.")
    
    return child

def mutate(individual, mutation_rate):
    mutated_genes = []

    for i, gene in enumerate(individual.genes):
        if random.random() < mutation_rate:
            new_gene = random.choice(['A', 'B', 'C', 'D'])
            print(f"{gene} mutated to {new_gene}.")
            mutated_genes.append(new_gene)
        else:
            mutated_genes.append(gene)

    return Individual(genes=mutated_genes)

def genetic_algorithm(target_length, population_size, mutation_rate, generations):
    population = [generate_individual(target_length) for _ in range(population_size)]

    for generation in range(generations):
        start_time = time.time()

        population.sort(key=lambda person: calculate_fitness(person), reverse=True)
        best_individual = population[0]
        total_time = round(time.time() - start_time, 2)

        print(f"Generation {generation + 1}, Best Individual: {best_individual.genes}, Total Time: {total_time} seconds")

        if calculate_fitness(best_individual) == target_length:
            print(f"Optimal Solution Found in terms of genes: {best_individual.genes}")
            break

        new_population = [best_individual]

        while len(new_population) < population_size:
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            new_population.append(child)

        population = new_population

if __name__ == "__main__":
    target_sequence_length = 4
    population_size = 100
    mutation_rate = 0.1
    generations = 100

    genetic_algorithm(target_sequence_length, population_size, mutation_rate, generations)
