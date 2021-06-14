from ListStructures.Queue import Queue

class Node:
    def __init__(self, state, action, parent, num_explored):
        self.state = state
        self.action = action
        self.parent = parent
        self.num_explored = num_explored

class Maze:
    def __init__(self, mazePath):
        mazeFile = open(mazePath)
        maze = mazeFile.read()
        mazeFile.close()
        self.maze = maze.splitlines()
        self.start, self.end, self.walls = self.getWalls()
        
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
        return start, end, walls

    def neighbors(self, state):
        row, col = state
        candidates = [
            ("up", (row+1, col)),
            ("right", (row, col-1)),
            ("down", (row-1, col)),
            ("left", (row, col+1))
        ]

        result = []

        for action, (r, c) in candidates:
            if 0 <= r and r < self.height and 0<= c and c<self.width and not self.walls[r][c]:
                result.append((action, (r, c)))

        
        return result

    def winCheck(self, state):
        if state == self.end:
            return True
    
    def solve(self):
        self.node = Node(self.start, ("start", self.start), None, 1)
        self.frontier = Queue()
        self.frontier.add(self.node)
        self.explored = []
        self.solutions = []
        self.solutionsOut = []

        while True:
            if self.frontier.isEmpty():
                break
            self.node = self.frontier.remove()
            if self.winCheck(self.node.state): 
                self.solutions.append(self.node)
                self.explored.append(self.node.state)
            else:
                self.explored.append(self.node.state)
                for action in self.neighbors(self.node.state):
                    if not(action[1] in self.explored):
                        self.frontier.add(Node(action[1], action[0], self.node, self.node.num_explored + 1))
        for solution in self.solutions:
            soluNode = solution
            num_explored = soluNode.num_explored
            solution = []
            while True:
                if soluNode.parent != None:
                    solution.append(soluNode.action)
                    soluNode = soluNode.parent
                else:
                    solution.reverse()
                    self.solutionsOut.append((solution, num_explored))
                    break
        return self.solutionsOut

if __name__ == "__main__":
    import sys
    maze = Maze(sys.argv[1])
    print(maze.solve())