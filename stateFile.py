class State:
    def __init__(self, state, parent, move, depth, cost, CumulativeCost):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost
        self.CumulativeCost = CumulativeCost
        if self.state:
            self.sequence = "".join(str(e) for e in self.state)

    # utility methods|
    def __eq__(self, other):
        return self.sequence == other.sequence

    def __lt__(self, other):
        return self.CumulativeCost < other.CumulativeCost
