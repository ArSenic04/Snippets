from collections import deque

# Function to display the solution path
def print_solution(path):
    for step in path:
        print(f"Jug1: {step[0]} liters, Jug2: {step[1]} liters")
    print()

# BFS function to solve the Water Jug problem
def bfs_solve(jug1_capacity, jug2_capacity, target):
    # Initial state: both jugs are empty
    initial_state = (0, 0)
    
    # Queue to store the states
    queue = deque()
    queue.append((initial_state, []))
    
    # Set to keep track of visited states
    visited = set()
    visited.add(initial_state)
    
    # BFS loop
    while queue:
        (current_state, path) = queue.popleft()
        
        (jug1, jug2) = current_state
        
        # Check if we have reached the target
        if jug1 == target or jug2 == target:
            print_solution(path + [(jug1, jug2)])
            return True
        
        # List of all possible actions (new states)
        possible_states = [
            (jug1_capacity, jug2),     # Fill jug1
            (jug1, jug2_capacity),     # Fill jug2
            (0, jug2),                 # Empty jug1
            (jug1, 0),                 # Empty jug2
            (min(jug1_capacity, jug1 + jug2), jug1 + jug2 - min(jug1_capacity, jug1 + jug2)),  # Pour jug2 into jug1
            (jug1 + jug2 - min(jug2_capacity, jug1 + jug2), min(jug2_capacity, jug1 + jug2))   # Pour jug1 into jug2
        ]
        
        # Explore each of the possible states
        for new_state in possible_states:
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [(jug1, jug2)]))
    
    return False

# Main function to run the simulation
def main():
    jug1_capacity = int(input("Enter the capacity of Jug 1: "))
    jug2_capacity = int(input("Enter the capacity of Jug 2: "))
    target = int(input("Enter the target amount of water: "))
    
    if not bfs_solve(jug1_capacity, jug2_capacity, target):
        print("No solution found.")

if __name__ == "__main__":
    main()
