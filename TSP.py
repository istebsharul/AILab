import itertools

def tsp(cities):
    # Generate all possible permutations of cities
    permutations = list(itertools.permutations(cities))
    
    # Initialize minimum distance and optimal route
    min_distance = float('inf')
    optimal_route = None
    
    # Iterate through all permutations
    for route in permutations:
        distance = 0
        
        # Calculate the total distance for the current route
        for i in range(len(route) - 1):
            distance += distance_between(route[i], route[i + 1])
        
        # Check if the current route has a shorter distance
        if distance < min_distance:
            min_distance = distance
            optimal_route = route
    
    return optimal_route, min_distance

# driver code
def distance_between(city1, city2):
    # Replace with your distance calculation logic
    return 0

# Example usage
cities = ['A', 'B', 'C', 'D']
optimal_route, min_distance = tsp(cities)
print("Optimal Route:", optimal_route)
print("Minimum Distance:", min_distance)
