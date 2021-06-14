from maze import Maze

class Node:
    def __init__(self, state, action, parent, num_explored):
        self.state = state
        self.action = action
        self.parent = parent
        self.num_explored = num_explored

class MazeGreedy():
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
        self.frontier = [self.node]
        self.explored = []

        while True:
            if not(self.frontier):
                break
            self.node = self.frontier[0]
            if len(self.frontier)!=1:
                for node in self.frontier:
                    if abs(node.state[0]-self.end[0])+abs(node.state[1]-self.end[1])+node.parent.num_explored+1>=abs(self.node.state[0]-self.end[0])+abs(self.node.state[1]-self.end[1])+node.parent.num_explored+1:
                        self.node = node

            self.frontier.remove(self.node)

            if self.winCheck(self.node.state): 
                break
            else:
                self.explored.append(self.node.state)
                for action in self.neighbors(self.node.state):
                    if not(action[1] in self.explored):
                        self.frontier.append(Node(action[1], action[0], self.node, self.node.num_explored + 1))
        soluNode = self.node
        # num_explored = soluNode.num_explored
        self.solution = []
        while True:
            if soluNode.parent != None:
                self.solution.append(soluNode.state)
                soluNode = soluNode.parent
            else:
                self.solution.reverse()
                break
        self.mazeSolved = self.maze
        for i in range(self.height):
            for j in range(self.width):
                if (i, j) in self.solution and (i, j) != self.end:
                    self.mazeSolved[i]=list(self.mazeSolved[i])
                    self.mazeSolved[i][j]="*"
                    self.mazeSolved[i]="".join(self.mazeSolved[i])
        self.mazeSolved = "\n".join(self.mazeSolved)
        return self.mazeSolved

if __name__ == "__main__":
    import sys
    maze = MazeGreedy(sys.argv[1])
    print(maze.solve())