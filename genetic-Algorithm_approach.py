import random
import time

random.seed(1)

class ZombieGameState:
    def __init__(self, individuals, bridge_capacity, total_time):
        self.individuals = individuals
        self.bridge_capacity = bridge_capacity
        self.total_time = total_time

def initialize_initial_state():
    # Factors
    individual_times = {chr(65 + i): random.randint(1, 10) for i in range(10)}  # A to J with random walking times
    bridge_capacity = 3
    total_time = sum(individual_times.values())  # Set total_time to the sum of individual walking times

    # Shuffle the order of individuals to represent a random initial state
    individuals_order = list(individual_times.keys())
    random.shuffle(individuals_order)

    # Create the initial state object
    initial_state = ZombieGameState(individuals=individuals_order, bridge_capacity=bridge_capacity, total_time=total_time)

    return initial_state, individual_times

def calculate_total_time(individuals, individual_times):
    return sum(individual_times[individual] for individual in individuals)

if __name__ == "__main__":
    start_time = time.time()

    initial_state, individual_times = initialize_initial_state()

    print("Initial State Representation:")
    print("Individuals and Walking Times:", [(individual, individual_times[individual]) for individual in initial_state.individuals])
    print("Bridge Capacity:", initial_state.bridge_capacity)
    print("Total Time:", initial_state.total_time, "minutes")

    # Genetic Algorithm approach

    # Population size initialization

    class Individual:
        def __init__(self, genes):
            self.genes = genes

    def generate_individual(individual_times):
        return Individual(genes=random.sample(list(individual_times.keys()), len(individual_times)))

    def initialize_population(population_size, individual_times):
        return [generate_individual(individual_times) for _ in range(population_size)]

    # Example usage:
    population_size = 50
    initial_population = initialize_population(population_size, individual_times)

    best_solution = None
    best_fitness = 0

    print("\nInitial Population:")
    for individual in initial_population:
        total_time = calculate_total_time(individual.genes, individual_times)
        print(f"Individual: {individual.genes}, Total Time: {total_time} minutes")

        # Evaluate fitness (you can modify this part based on your criteria)
        fitness = 0
        if total_time <= initial_state.total_time:
            fitness = len(set(individual.genes))  # Fitness based on unique genes

        if fitness > best_fitness:
            best_solution = individual
            best_fitness = fitness

    end_time = time.time()
    total_time_taken = round(end_time - start_time, 2)
    print(f"\nTotal Time Taken for Initialization: {total_time_taken} seconds")

    # Print the optimal solution
    print("\nOptimal Solution:")
    print("Individuals and Walking Times:", [(individual, individual_times[individual]) for individual in best_solution.genes])
    print("Total Time:", calculate_total_time(best_solution.genes, individual_times), "minutes")
