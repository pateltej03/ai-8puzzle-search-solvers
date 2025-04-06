import heapq
from collections import deque
import math


# Goal state
goalState = ['_', '1', '2', '3', '4', '5', '6', '7', '8']
expansions = 0

# Helper function to read the initial state from 'input.txt'
def read_input():

    with open("input.txt", 'r') as file:
        initial_state = file.read().split(",")
    return initial_state


# Helper function to get the neighbors of the blank tile
def get_newState_and_move(state):

    index = state.index('_')
    newStateAndMove = []

    if index % 3 != 0:  # Blank Tile can move left, so new_state[index] moves right
        new_state = state.copy()
        new_state[index], new_state[index - 1] = new_state[index - 1], new_state[index]
        newStateAndMove.append((new_state, new_state[index] + "R"))

    if index % 3 != 2:  # Blank Tile can move right, so new_state[index] moves left
        new_state = state.copy()
        new_state[index], new_state[index + 1] = new_state[index + 1], new_state[index]
        newStateAndMove.append((new_state, new_state[index] + "L"))

    if index >= 3:  # Blank Tile can move up, so new_state[index] moves down
        new_state = state.copy()
        new_state[index], new_state[index - 3] = new_state[index - 3], new_state[index]
        newStateAndMove.append((new_state, new_state[index] + "D"))

    if index <= 5:  # Blank Tile can move down, so new_state[index] moves up
        new_state = state.copy()
        new_state[index], new_state[index + 3] = new_state[index + 3], new_state[index]
        newStateAndMove.append((new_state, new_state[index] + "U"))

    return newStateAndMove



def DFS(initial_state):
    global expansions
    
    stack = [(initial_state, [])]
    visited = set()
    visited.add(tuple(initial_state))

    while stack:
        current_state, path = stack.pop()

        if current_state == goalState:
            return path

        for newState, move in get_newState_and_move(current_state):
            if tuple(newState) not in visited:
                visited.add(tuple(newState))
                stack.append((newState, path + [move]))
                
                expansions += 1


    return None



def BFS(initial_state):
    global expansions
    
    queue = deque([(initial_state, [])])
    visited = set()
    visited.add(tuple(initial_state))

    while queue:
        current_state, path = queue.popleft()

        if current_state == goalState:
            return path

        for newState, move in get_newState_and_move(current_state):

            if tuple(newState) not in visited:
                visited.add(tuple(newState))
                queue.append((newState, path + [move]))
                
                expansions += 1

    return None



def UCS(initial_state):
    global expansions
    
    priority_queue = [(0, initial_state, [])]  # (cost, state, path)
    visited = set()
    visited.add(tuple(initial_state))

    while priority_queue:
        cost, current_state, path = heapq.heappop(priority_queue)

        if current_state == goalState:
            return path

        for newState, move in get_newState_and_move(current_state):

            if tuple(newState) not in visited:
                visited.add(tuple(newState))
                heapq.heappush(priority_queue, (cost + 1, newState, path + [move]))
                
                expansions += 1

    return None



# Heuristic: Manhattan distance
def manhattan_distance(state):

    total = 0

    for i, tile in enumerate(state):

        if tile != '_':

            goal_pos = goalState.index(tile)
            total += abs((i // 3) - (goal_pos // 3)) + abs((i % 3) - (goal_pos % 3)) # absolute y distance + absolute x distance 

    return total



# A* implementation with Manhattan Distance,
# logic is such that, higher cumulative manhattan distance is given lower priority
def AStar1(initial_state):
    global expansions
    
    priority_queue = [(manhattan_distance(initial_state), 0, initial_state, [])]
    visited = set()
    visited.add(tuple(initial_state))

    while priority_queue:
        est_total_cost, cost, current_state, path = heapq.heappop(priority_queue)

        if current_state == goalState:
            return path
            
        for newState, move in get_newState_and_move(current_state):

            if tuple(newState) not in visited:
                visited.add(tuple(newState))
                new_cost = cost + 1
                heapq.heappush(priority_queue, (new_cost + manhattan_distance(newState), new_cost, newState, path + [move]))
                
                expansions += 1

    return None



# Heuristic: Straight Line Distance 
def straight_line_distance(state):

    total = 0

    for i, tile in enumerate(state):

        if tile != '_':

            goal_pos = goalState.index(tile)
            # absolute y distance
            y = abs((i // 3) - (goal_pos // 3))
            # absolute x distance
            x = abs((i % 3) - (goal_pos % 3))
            total += math.hypot(x, y) # straight line distance is hypotenuse, as they are all essentially 90 degree traingles.

    return total



# A* implementation with Straight Line Distance
# logic is such that, higher cumulative manhattan distance is given lower priority
def AStar2(initial_state):
    global expansions
    
    priority_queue = [(straight_line_distance(initial_state), 0, initial_state, [])]
    visited = set()
    visited.add(tuple(initial_state))

    while priority_queue:
        est_total_cost, cost, current_state, path = heapq.heappop(priority_queue)

        if current_state == goalState:
            return path

        for newState, move in get_newState_and_move(current_state):

            if tuple(newState) not in visited:
                visited.add(tuple(newState))
                new_cost = cost + 1
                heapq.heappush(priority_queue, (new_cost + straight_line_distance(newState), new_cost, newState, path + [move]))
                
                expansions += 1

    return None



# Main function to execute the searches
def main():
    global expansions
    initial_state = read_input()
    # print("initial_state from input.txt:", initial_state)

    # Run DFS
    print("The solution of Q1.1a is:")
    print(",".join(DFS(initial_state)))
    # print("Node expansions:", expansions)
    
    expansions = 0

    # Run BFS
    print("The solution of Q1.1b is:")
    print(",".join(BFS(initial_state)))
    # print("Node expansions:", expansions)
    
    expansions = 0

    # Run UCS
    print("The solution of Q1.1c is:")
    print(",".join(UCS(initial_state)))
    # print("Node expansions:", expansions)
    
    expansions = 0

    # Run A* (Manhattan Distance)
    print("The solution of Q1.1d is:")
    print(",".join(AStar1(initial_state)))
    # print("Node expansions:", expansions)
    
    expansions = 0

    # Run A* (Straight Line Distance)
    print("The solution of Q1.1e is:")
    print(",".join(AStar2(initial_state)))
    # print("Node expansions:", expansions)
    
    expansions = 0



if __name__ == "__main__":
    main()
