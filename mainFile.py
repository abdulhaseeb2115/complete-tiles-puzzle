import heapq
from utilityFile import printNode, getMisplacedTiles, getInvCount
from stateFile import State


# Variables
total_tiles = 9
rows_cols = 3
moves = 0

start_state = list()
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
solution = list()
goal_node = State

explored = list()
frontier = list()
heap_dictionary = {}

max_depth = 0
expanded = 0
generated = 0


# Get Input(get starting state from user)
def getInput():
    print(
        "--------------------------------------------------------------------\n"
        + "\nProgram accepts input in following format('0' is used as empty tile)"
        + "\n1 2 3\n4 5 6\n7 8 0"
        + "\n\nEnter Start State:"
    )
    for x in range(0, 3):
        input_sequence = input("")
        startState = input_sequence.split(" ")
        for element in startState:
            start_state.append(int(element))

    print("\n=Start=")
    printNode(start_state, False)
    print("\n=======")


# Print Solution(steps and information)
def printSolution():
    global generated
    generated = len(frontier) + len(explored)
    backtrace()
    solution.reverse()

    # traverse solution for nodes|
    # printing nodes|
    # printing information|
    print()
    for node in solution:
        if solution.index(node) == len(solution) - 1:
            printNode(node.state, False)
        else:
            printNode(node.state, True)

    print(
        "\n=======\n\n->Goal State !\n---------------------------\n Path Cost: ", moves
    )
    print(" Total Nodes Generated: " + str(generated))
    print(" Total Nodes Explored: " + str(expanded))
    print("---------------------------\n")


# Backtrace(backtracing to get solution)
def backtrace():
    global moves, solution
    current_node = goal_node
    solution.append(current_node)

    # backtracing in the list|
    # increase moves|
    # get parent nodes|
    # append them to solution|
    while start_state != current_node.state:
        moves = moves + 1
        current_node = current_node.parent
        solution.append(current_node)
    return moves


# Main Function(Using A*)
def process():
    global goal_node, max_depth, expanded
    heuristic_value = getMisplacedTiles(start_state, goal_state)

    # first create the start node|
    # then heapify the frontier|
    # then push the node to the heap|
    # then store sequences of nodes as a dictionary|
    StartNode = State(start_state, None, None, 0, 0, heuristic_value)
    heapq.heapify(frontier)
    heapq.heappush(frontier, StartNode)
    heap_dictionary[StartNode.sequence] = StartNode

    # loop for testing nodes|
    while frontier:
        heapq.heapify(frontier)
        popped_node = heapq.heappop(frontier)
        explored.append(popped_node)
        expanded += 1

        # check if goal|
        # if true set equal to the popped node |
        if popped_node.state == goal_state:
            goal_node = popped_node
            return frontier

        # if goal not found|
        # continue to expand and store nodes|
        neighbors = expand(popped_node)

        for neighbor in neighbors:
            neighbor.CumulativeCost = (
                getMisplacedTiles(neighbor.state, goal_state) + neighbor.cost
            )

            # check if already explored|
            # if not explored and not in frontier|
            # push to frontier and dictionary|
            if neighbor not in explored:
                if neighbor not in frontier:
                    heapq.heappush(frontier, neighbor)
                    heap_dictionary[neighbor.sequence] = neighbor
                    # depth++
                    if neighbor.depth > max_depth:
                        max_depth += 1

                elif (
                    neighbor in frontier
                    and neighbor.CumulativeCost
                    < frontier[frontier.index(neighbor)].CumulativeCost
                ):
                    frontier[frontier.index(neighbor)] = neighbor
                    heap_dictionary[neighbor.sequence] = neighbor
                    heapq.heapify(frontier)

                    # depth++
                    if neighbor.depth > max_depth:
                        max_depth += 1

        # heapify the frontier|
        heapq.heapify(frontier)


# Expand Nodes(all possible moves list)
def expand(node):
    neighbors = list()
    neighbors.append(
        State(move(node.state, 1), node, 1, node.depth + 1, node.cost + 1, 0)
    )
    neighbors.append(
        State(move(node.state, 2), node, 2, node.depth + 1, node.cost + 1, 0)
    )
    neighbors.append(
        State(move(node.state, 3), node, 3, node.depth + 1, node.cost + 1, 0)
    )
    neighbors.append(
        State(move(node.state, 4), node, 4, node.depth + 1, node.cost + 1, 0)
    )
    nodes = [neighbor for neighbor in neighbors if neighbor.state]
    return nodes


# Move Node(moves in puzzle)
def move(state, position):
    new_state = state[:]
    index = new_state.index(0)
    # up
    if position == 1:
        if index not in range(0, rows_cols):
            temp = new_state[index - rows_cols]
            new_state[index - rows_cols] = new_state[index]
            new_state[index] = temp
            return new_state
        else:
            return None

    # down
    if position == 2:
        if index not in range(total_tiles - rows_cols, total_tiles):
            temp = new_state[index + rows_cols]
            new_state[index + rows_cols] = new_state[index]
            new_state[index] = temp
            return new_state
        else:
            return None

    # left
    if position == 3:
        if index not in range(0, total_tiles, rows_cols):
            temp = new_state[index - 1]
            new_state[index - 1] = new_state[index]
            new_state[index] = temp
            return new_state
        else:
            return None

    # right
    if position == 4:
        if index not in range(rows_cols - 1, total_tiles, rows_cols):
            temp = new_state[index + 1]
            new_state[index + 1] = new_state[index]
            new_state[index] = temp
            return new_state
        else:
            return None


def main():
    getInput()

    # check if puzzle is solvable|
    # if true start process|
    # else print message|
    if getInvCount(start_state) % 2 != 0:
        print(
            "\n--> Puzzle is not solvable !\n--> (it has odd number of conversions)\n"
        )
    else:
        print("\nProgram Running(Don't Close)")
        process()
        printSolution()

    print(
        "============================\n"
        + "8 Tiles Puzzle Project (A*)\nFA19-BSE-091|092|090|086|\n"
        + "============================\n\n\n\n"
    )


if __name__ == "__main__":
    main()
