import heapq

# Node class representing a state in the search space
class Node:
    def __init__(self, state, g_cost, h_cost, parent=None):
        self.state = state  # Current state
        self.g_cost = g_cost  # Cost from start node to current node
        self.h_cost = h_cost  # Heuristic cost from current node to goal node
        self.parent = parent  # Parent node

    def f_cost(self):
        return self.g_cost + self.h_cost

# AO* algorithm
def ao_star(start_state, goal_state, heuristic_fn, successors_fn):
    # Initialize the open list as a priority queue
    open_list = []
    heapq.heappush(open_list, (0, Node(start_state, 0, heuristic_fn(start_state))))

    while open_list:
        # Get the node with the lowest f_cost from the open list
        _, current_node = heapq.heappop(open_list)

        if current_node.state == goal_state:
            # Goal state reached, return the path
            return get_path(current_node)

        for successor_state, action_cost in successors_fn(current_node.state):
            g_cost = current_node.g_cost + action_cost
            h_cost = heuristic_fn(successor_state)
            f_cost = g_cost + h_cost

            # Check if the successor state is already in the open list
            # If so, update its costs if the new path is better
            in_open_list = False
            for _, node in open_list:
                if node.state == successor_state:
                    in_open_list = True
                    if f_cost < node.f_cost():
                        open_list.remove((node.f_cost(), node))
                        heapq.heapify(open_list)
                        heapq.heappush(open_list, (f_cost, Node(successor_state, g_cost, h_cost, current_node)))
                    break

            if not in_open_list:
                heapq.heappush(open_list, (f_cost, Node(successor_state, g_cost, h_cost, current_node)))

    # No path found
    return None

# Helper function to reconstruct the path
def get_path(node):
    path = []
    while node:
        path.insert(0, node.state)
        node = node.parent
    return path

# Example usage
start_state = 1
goal_state = 10

# Heuristic function
def heuristic(state):
    return abs(state - goal_state)

# Successors function
def successors(state):
    successors = []
    successors.append((state + 1, 1))  # Move to the right with cost 1
    successors.append((state - 1, 1))  # Move to the left with cost 1
    return successors

# Run AO* algorithm
path = ao_star(start_state, goal_state, heuristic, successors)
if path:
    print("Path found:", path)
else:
    print("No path found.")
