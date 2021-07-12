class Board():
    def __init__(self, data):
        self.initial = data
        self.board = data
        self.services, self.houses = self.getData(self.board)
    
    def getData(self, board):
        houses = [(x, y) for y in range(len(board)) for x in board[y] if board[y][x] == 'H']
        services = [(x, y) for y in range(len(board)) for x in board[y] if board[y][x] == 'S']
        return services, houses

    def hillClimb(self, node):
        current = node
        while True:
            sortedList = []
            if current.frontier == []:
                return current
            for state in current.frontier:
                sortedList.append({'state': state, 'v': state.value})
            sortedList = sorted(sortedList, key=lambda k: k['v'])
            worst = sortedList[0]['state']
            frontier = [State(neighbour, self) for neighbour in self.neighbours(worst) if State(neighbour, self).value >= current.value]
            for neighbour in self.neighbours(worst):
                frontier.append(State(neighbour, self))
            explored = node.explored
            explored.append(worst)
            current = Node(worst, frontier, explored)

    def neighbours(self, state):
        possible = [
            (state.location[0]+1, state.loaction[1]),
            (state.location[0]-1, state.loaction[1]),
            (state.location[0], state.loaction[1]-1),
            (state.location[0], state.loaction[1]+1)
        ]
        return [location for location in possible if not(location in self.houses)]

    def solve(self):
        for _ in self.services:
            pass

class State():
    def __init__(self, location, board):
        self.location = location
        self.value = 0
        for house in board.houses:
            self.value += abs(self.location[0])-abs(house[0]) + abs(self.location[1])-abs(house[1])

class Node():
    def __init__(self, state, frontier, explored):
        self.state = state
        self.frontier = frontier
        self.explored = explored
