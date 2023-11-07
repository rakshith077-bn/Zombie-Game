# Constants
people = {1: 1, 2: 2, 3: 5, 4: 10}  # Mapping people to their respective crossing times
lantern_capacity = 2
zombies_time = 17

# Initialize variables
time_elapsed = 0
crossed = []

# Helper function for crossing the bridge
def cross_bridge(people_to_cross, time_elapsed):
    if len(people_to_cross) == 1:
        return time_elapsed + people_to_cross[0]

    if len(people_to_cross) == 2:
        return time_elapsed + max(people_to_cross)

# Backtracking algorithm to find the optimal solution
def escape_bridge(people_to_cross, time_elapsed, crossed):
    if time_elapsed >= zombies_time:
        return False

    if not people_to_cross:
        return True

    for group in range(1, lantern_capacity + 1):
        for crossing_group in combinations(people_to_cross, group):
            remaining_people = [p for p in people_to_cross if p not in crossing_group]
            time_taken = cross_bridge(crossing_group, time_elapsed)
            if time_taken > zombies_time:
                continue

            crossed.append(crossing_group)
            if escape_bridge(remaining_people, time_taken, crossed):
                return True
            crossed.pop()
    return False

# Run the backtracking algorithm
from itertools import combinations

people_to_cross = list(people.values())
escape_possible = escape_bridge(people_to_cross, time_elapsed, crossed)

# Output the results
if escape_possible:
    for idx, group in enumerate(crossed):
        print(f"Group {idx + 1}: {group} crossed the bridge in {cross_bridge(group, time_elapsed)} minutes")
else:
    print("It is not possible to escape within the time limit.")
