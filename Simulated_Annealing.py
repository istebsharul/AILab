import math
import random

# Objective function
def objective_function(x):
    return x**2

# Simulated Annealing algorithm
def simulated_annealing(initial_solution, temperature, cooling_rate, iterations):
    current_solution = initial_solution
    best_solution = current_solution

    for i in range(iterations):
        temperature *= cooling_rate

        # Generate a neighboring solution
        neighbor = current_solution + random.uniform(-1, 1)

        # Calculate the objective function values
        current_value = objective_function(current_solution)
        neighbor_value = objective_function(neighbor)

        # Determine if the neighbor is accepted as the new solution
        if neighbor_value < current_value:
            current_solution = neighbor
        else:
            acceptance_probability = math.exp((current_value - neighbor_value) / temperature)
            if random.random() < acceptance_probability:
                current_solution = neighbor

        # Update the best solution
        if objective_function(current_solution) < objective_function(best_solution):
            best_solution = current_solution

    return best_solution

# Example usage
initial_solution = random.uniform(-10, 10)
temperature = 100
cooling_rate = 0.95
iterations = 1000

best_solution = simulated_annealing(initial_solution, temperature, cooling_rate, iterations)
best_value = objective_function(best_solution)

print("Best Solution:", best_solution)
print("Best Value:", best_value)
