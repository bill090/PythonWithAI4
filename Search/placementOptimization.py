class Board():
    def __init__(self, data):
        self.board = data
        self.services, self.houses = self.getData(self.board)
        self.width = len(data)
        self.height = max([len(line) for line in data])
    
    def getData(self, board):
        houses = [(x, y) for y in range(len(board)) for x in range(len(board[y])) if board[y][x] == 'H']
        services = [(x, y) for y in range(len(board)) for x in range(len(board[y])) if board[y][x] == 'S']
        return services, houses
    
    def moveService(self, location, newlocation):
        new = self.board
        new[newlocation[1]][newlocation[0]] = 'S'
        new[location[1]][location[0]] = ' '
        self.board = new
        self.services, self.houses = self.getData(self.board)
        

    def showBoard(self):
        for i in self.board:
            for j in i:
                print(j, end='')
            print()

    def availiableSpaces(self):
        [(x, y) for y in len(range(self.board)) for x in len(range(self.board[y])) if self.board[y][x] == ' ']

    def neighbours(self, location):
        possible = [
            (location[0]+1, location[1]),
            (location[0]-1, location[1]),
            (location[0], location[1]-1),
            (location[0], location[1]+1)
        ]
        return [location for location in possible if not(location in self.houses or location in self.services)]

    def solve(self, maximum=None):
        count = 0
        while maximum == None or count <= maximum:
            new = []
            for service in self.services:
                possible = []
                for neighbour in self.neighbours(service):
                    if self.getCost(neighbour) > self.getCost(service) and not(neighbour in new):
                        possible.append(neighbour)
                try:
                    new.append(sorted(possible, key=self.getCost)[0])
                except:
                    pass
                if possible != []:
                    self.moveService(service, new[-1])
            
            self.showBoard()
            
            if new == []:
                break
        
        self.showBoard()
        return self.services, self.board
    
    def getCost(self, location):
        out = 0
        for house in self.houses:
            out += abs(house[0]-location[0])+abs(house[1]-location[1])
        return out * -1

class State():
    def __init__(self, location, board):
        self.location = location
        self.value = 0
        for house in board.houses:
            self.value += abs(self.location[0])-abs(house[0]) + abs(self.location[1])-abs(house[1])

if __name__ == "__main__":
    file_name = input()
    dataFile = open(file_name)
    data = dataFile.read()
    dataFile.close()
    dataIn = []
    for line in data.splitlines():
        dataIn.append([char for char in line])
    board = Board(dataIn)
    board.solve()
    board.showBoard()
