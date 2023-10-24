# Print Node(matrix shape)
def printNode(listpuzzle, display):
    for tile in listpuzzle:
        if listpuzzle.index(tile) % 3 == 0 and listpuzzle.index(tile) != 0:
            print("")
        print(" " + str(tile), end="")

    if display:
        print("\n")


# Misplaced Tiles (calculating heuristic value)
def getMisplacedTiles(node_list, goal_state):
    misplacedTiles = 0
    for iter in range(0, len(node_list)):
        if node_list[iter] == 0:
            continue
        elif node_list[iter] != goal_state[iter]:
            misplacedTiles = misplacedTiles + 1

    return misplacedTiles


# Get Inversions Count(to check if puzzle is solvable)
def getInvCount(start_state):
    count = 0
    empty = 0
    for i in range(0, 9):
        for j in range(i + 1, 9):
            if (
                start_state[j] != empty
                and start_state[i] != empty
                and start_state[i] > start_state[j]
            ):
                count += 1
    return count
