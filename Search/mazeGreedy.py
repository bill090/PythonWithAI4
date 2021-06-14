from maze import Maze, Node
class State():
    def __init__(self, pos, end):
        self.pos = pos
        self.manhattanVal = abs(pos[0] - end[0]) + abs(pos[1] - end[1])

class MazeGreedy(Maze):
    super().__init__()
    
    def getWalls(self):
        self.height = len(self.maze)
        self.width = max(len(line) for line in self.maze)
        walls = []

        for i in range(self.height):
            row = []
            try:
                for j in range(self.width):
                    if self.maze[i][j] == "A":
                        row.append(False)
                        start = (i, j)
                    elif self.maze[i][j] == "B":
                        row.append(False)
                        end = (i, j)
                    elif self.maze[i][j] == " ":
                        row.append(False)
                    else:
                        row.append(True)
            except IndexError:
                row.append(False)
            walls.append(row)
        self.start = State(self.start, self.end)
        self.end = State(self.end, self.end)
        return start, end, walls

    def neighbors(self, state):
        row, col = state
        candidates = [
            ("down", (row+1, col)),
            ("left", (row, col-1)),
            ("up", (row-1, col)),
            ("right", (row, col+1))
        ]

        result = []

        for action, (r, c) in candidates:
            if 0 <= r and r < self.height and 0<= c and c<self.width and not self.walls[r][c]:
                result.append((action, State((r, c), self.end)))

        
        return result

    def solve(self):
        self.node = Node(self.start, ("start", self.start), None, 1)
        self.frontier = [self.node]
        self.explored = []

        while True:
            if self.frontier.isEmpty():
                return("There is no solution")
            out = self.frontier[0]
            for node in self.frontier:
                if node.state.manhattanVal >= out:
                    out = node
            self.frontier.remove(out)
            self.node = out
            if self.winCheck(self.node.state):
                break
            else:
                self.explored.append(self.node.state)
                for action in self.neighbors(self.node.state):
                    if not(action[1] in self.explored):
                        self.frontier.add(Node(action[1], action[0], self.node, self.node.num_explored + 1))
        soluNode = self.node
        num_explored = soluNode.num_explored
        self.solution = []
        while True:
            if soluNode.parent != None:
                self.solution.append(soluNode.action)
                soluNode = soluNode.parent
            else:
                self.solution.reverse()
                return self.solution, num_explored

if __name__ == "__main__":
    import sys
    maze = Maze(sys.argv[1])
    print(maze.solve())