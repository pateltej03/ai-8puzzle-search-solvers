import heapq
from collections import deque
import math


expansions = 0

# Goal State
def is_goal(state):
    top_row = state[:3]
    top_sum = 0
    for x in top_row:
        if x != '_':
            top_sum += int(x)

    if top_sum == 11:
        return True
    else:
        return False


states_with_top_row_sum_eleven = [
    ["8","3","_","_","_","_","_","_","_"],
    ["8","_","3","_","_","_","_","_","_"],
    ["_","3","8","_","_","_","_","_","_"],
    ["_","8","3","_","_","_","_","_","_"],
    ["3","_","8","_","_","_","_","_","_"],
    ["3","8","_","_","_","_","_","_","_"],
    
    ["8","2","1","_","_","_","_","_","_"],
    ["8","1","2","_","_","_","_","_","_"],
    ["2","8","1","_","_","_","_","_","_"],
    ["2","1","8","_","_","_","_","_","_"],
    ["1","2","8","_","_","_","_","_","_"],
    ["1","8","2","_","_","_","_","_","_"],

    ["7","4","_","_","_","_","_","_","_"],
    ["7","_","4","_","_","_","_","_","_"],
    ["4","7","_","_","_","_","_","_","_"],
    ["4","_","7","_","_","_","_","_","_"],
    ["_","4","7","_","_","_","_","_","_"],
    ["_","7","4","_","_","_","_","_","_"],
    
    ["7","3","1","_","_","_","_","_","_"],
    ["7","1","3","_","_","_","_","_","_"],
    ["3","7","1","_","_","_","_","_","_"],
    ["3","1","7","_","_","_","_","_","_"],
    ["1","7","3","_","_","_","_","_","_"],
    ["1","3","7","_","_","_","_","_","_"],
    
    ["6","5","_","_","_","_","_","_","_"],
    ["6","_","5","_","_","_","_","_","_"],
    ["5","6","_","_","_","_","_","_","_"],
    ["5","_","6","_","_","_","_","_","_"],
    ["_","5","6","_","_","_","_","_","_"],
    ["_","6","5","_","_","_","_","_","_"],

    ["6","4","1","_","_","_","_","_","_"],
    ["6","1","4","_","_","_","_","_","_"],
    ["4","1","6","_","_","_","_","_","_"],
    ["4","6","1","_","_","_","_","_","_"],
    ["1","4","6","_","_","_","_","_","_"],
    ["1","6","4","_","_","_","_","_","_"],

    ["6","3","2","_","_","_","_","_","_"],
    ["6","2","3","_","_","_","_","_","_"],
    ["3","6","2","_","_","_","_","_","_"],
    ["3","2","6","_","_","_","_","_","_"],
    ["2","3","6","_","_","_","_","_","_"],
    ["2","6","3","_","_","_","_","_","_"],

    ["5","4","2","_","_","_","_","_","_"],
    ["5","2","4","_","_","_","_","_","_"],
    ["4","5","2","_","_","_","_","_","_"],
    ["4","2","5","_","_","_","_","_","_"],
    ["2","4","5","_","_","_","_","_","_"],
    ["2","5","4","_","_","_","_","_","_"],
    
]

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

        if is_goal(current_state):
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

        if is_goal(current_state):
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

        if is_goal(current_state):
            return path

        for newState, move in get_newState_and_move(current_state):

            if tuple(newState) not in visited:
                visited.add(tuple(newState))
                heapq.heappush(priority_queue, (cost + 1, newState, path + [move]))
                expansions += 1

    return None

# Heuristic: Manhattan distance, for sum  11
def goal_manhattan_distance(state):
    goalState = state.copy()
    lowestCost = 100
    for temp_state in states_with_top_row_sum_eleven:
        stateCost = vanilla_manhattan_distance(temp_state, goalState)
        if stateCost < lowestCost:
            lowestCost = stateCost
    return lowestCost

# Heuristic: Manhattan distance
def vanilla_manhattan_distance(state, goalState):
    
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
    
    priority_queue = [(goal_manhattan_distance(initial_state), 0, initial_state, [])]
    visited = set()
    visited.add(tuple(initial_state))

    while priority_queue:
        est_total_cost, cost, current_state, path = heapq.heappop(priority_queue)

        if is_goal(current_state):
            return path
            
        for newState, move in get_newState_and_move(current_state):

            if tuple(newState) not in visited:
                visited.add(tuple(newState))
                new_cost = cost + 1
                heapq.heappush(priority_queue, (new_cost + goal_manhattan_distance(newState), new_cost, newState, path + [move]))
                expansions += 1

    return None



# Heuristic: Manhattan distance, for sum  11
def goal_straight_line_distance(state):
    goalState = state.copy()
    lowestCost = 100
    for temp_state in states_with_top_row_sum_eleven:
        stateCost = vanilla_straight_line_distance(temp_state, goalState)
        if stateCost < lowestCost:
            lowestCost = stateCost
    return lowestCost

# Heuristic: Straight Line Distance 
def vanilla_straight_line_distance(state, goalState):

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
    
    priority_queue = [(goal_straight_line_distance(initial_state), 0, initial_state, [])]
    visited = set()
    visited.add(tuple(initial_state))

    while priority_queue:
        est_total_cost, cost, current_state, path = heapq.heappop(priority_queue)

        if is_goal(current_state):
            return path

        for newState, move in get_newState_and_move(current_state):

            if tuple(newState) not in visited:
                visited.add(tuple(newState))
                new_cost = cost + 1
                heapq.heappush(priority_queue, (new_cost + goal_straight_line_distance(newState), new_cost, newState, path + [move]))
                expansions += 1

    return None



# Main function to execute the searches
def main():
    global expansions
    initial_state = read_input()
    print("initial_state from input.txt:", initial_state)

    # Run DFS
    print("The solution of Q2.1a is:")
    print(",".join(DFS(initial_state)))
    # print("Node expansions:", expansions)
    expansions = 0

    # Run BFS
    print("The solution of Q2.1b is:")
    print(",".join(BFS(initial_state)))
    # print("Node expansions:", expansions)
    expansions = 0

    # Run UCS
    print("The solution of Q2.1c is:")
    print(",".join(UCS(initial_state)))
    # print("Node expansions:", expansions)
    expansions = 0

    # Run A* (Manhattan Distance)
    print("The solution of Q2.1d is:")
    print(",".join(AStar1(initial_state)))
    # print("Node expansions:", expansions)
    expansions = 0

    # Run A* (Straight Line Distance)
    print("The solution of Q2.1e is:")
    print(",".join(AStar2(initial_state)))
    # print("Node expansions:", expansions)
    expansions = 0



if __name__ == "__main__":
    main()
