import random
import math

class ZombieGameState:
    def __init__(self, individuals, bridge_capacity, total_time):
        self.individuals = individuals
        self.bridge_capacity = bridge_capacity
        self.total_time = total_time

def initialize_initial_state():
    # Factors
    individual_times = {'A': 1, 'B': 2, 'C': 5, 'D': 10}
    bridge_capacity = 2
    total_time = 17

    # Shuffle the order of individuals to represent a random initial state
    individuals_order = list(individual_times.keys())
    random.shuffle(individuals_order)

    # Create the initial state object
    initial_state = ZombieGameState(individuals=individuals_order, bridge_capacity=bridge_capacity, total_time=total_time)

    return initial_state, individual_times

def calculate_fitness(state):
    total_time = sum([individual_times[individual] for individual in state.individuals])
    return total_time

def generate_neighbor(current_state):
    # Swap two random individuals to generate a neighboring state
    new_state = ZombieGameState(individuals=current_state.individuals.copy(),
                                bridge_capacity=current_state.bridge_capacity,
                                total_time=current_state.total_time)
    
    index1, index2 = random.sample(range(len(new_state.individuals)), 2)
    new_state.individuals[index1], new_state.individuals[index2] = new_state.individuals[index2], new_state.individuals[index1]

    return new_state

def simulated_annealing(initial_state, temperature, cooling_rate, max_iterations):
    current_state = initial_state
    best_state = initial_state
    iteration = 0

    while temperature > 0 and iteration < max_iterations:
        neighbor_state = generate_neighbor(current_state)
        delta_fitness = calculate_fitness(neighbor_state) - calculate_fitness(current_state)

        if delta_fitness < 0 or random.uniform(0, 1) < math.exp(-delta_fitness / temperature):
            current_state = neighbor_state

        if calculate_fitness(current_state) < calculate_fitness(best_state):
            best_state = current_state

        # Print information about each iteration
        print(f"Iteration {iteration + 1}:")
        print("Current State - Individuals and Walking Times:", [(individual, individual_times[individual]) for individual in current_state.individuals])
        print("Current Fitness:", calculate_fitness(current_state))

        temperature *= cooling_rate
        iteration += 1

    return best_state

if __name__ == "__main__":
    initial_state, individual_times = initialize_initial_state()

    print("Initial State Representation:")
    print("Individuals and Walking Times:", [(individual, individual_times[individual]) for individual in initial_state.individuals])
    print("Bridge Capacity:", initial_state.bridge_capacity)
    print("Total Time:", initial_state.total_time)

    # Simulated Annealing approach
    initial_temperature = 100.0
    cooling_rate = 0.99
    max_iterations = 1000

    final_state = simulated_annealing(initial_state, initial_temperature, cooling_rate, max_iterations)

    print("\nSimulated Annealing Result:")
    print("Best State - Individuals and Walking Times:", [(individual, individual_times[individual]) for individual in final_state.individuals])
    print("Bridge Capacity:", final_state.bridge_capacity)
    print("Total Time:", final_state.total_time)
    print("Best Fitness:", calculate_fitness(final_state))
