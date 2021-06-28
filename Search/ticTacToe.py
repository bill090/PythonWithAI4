class Board:
    def __init__(self, player = 1, board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]):
        self.board = board
        self.turn = 1
        self.player = player
    def action(self, pos, player):
        if self.board[pos[0]][pos[1]] != 0:
            raise Exception("Position was already played on.")
        else:
            newBoard = self.board
            newBoard[pos[0]][pos[1]] += player
            return newBoard
    def actions(self):
        return [(x, y) for y in range(len(self.board)) for x in range(len(self.board)) if self.board[x][y] == 0]
    def utility(self):
        if (self.board[0][0] == 1 and self.board[1][0] == 1 and self.board[2][0] == 1) or (self.board[0][1] == 1 and self.board[1][1] == 1 and self.board[2][1] == 1) or (self.board[0][2] == 1 and self.board[1][2] == 1 and self.board[2][2] == 1):
            return 1
        if (self.board[0][0] == 1 and self.board[0][1] == 1 and self.board[0][2] == 1) or (self.board[1][0] == 1 and self.board[1][1] == 1 and self.board[1][2] == 1) or (self.board[2][0] == 1 and self.board[2][1] == 1 and self.board[2][2] == 1):
            return 1
        if (self.board[0][0] == 1 and self.board[1][1] == 1 and self.board[2][2] == 1) or (self.board[2][0] == 1 and self.board[1][1] == 1 and self.board[0][2] == 1):
            return 1
        if (self.board[0][0] == -1 and self.board[1][0] == -1 and self.board[2][0] == -1) or (self.board[0][1] == -1 and self.board[1][1] == -1 and self.board[2][1] == -1) or (self.board[0][2] == -1 and self.board[1][2] == -1 and self.board[2][2] == -1):
            return -1
        if (self.board[0][0] == -1 and self.board[0][1] == -1 and self.board[0][2] == -1) or (self.board[1][0] == -1 and self.board[1][1] == -1 and self.board[1][2] == -1) or (self.board[2][0] == -1 and self.board[2][1] == -1 and self.board[2][2] == -1):
            return -1
        if (self.board[0][0] == -1 and self.board[1][1] == -1 and self.board[2][2] == -1) or (self.board[2][0] == -1 and self.board[1][1] == -1 and self.board[0][2] == -1):
            return -1
        return 0
    def playerToMove(self):
        x = 0
        o = 0
        for i in self.board:
            for j in self.board[i]:
                if j == 1:
                    x += 1
                if j == -1:
                    o += 1
        if x > o:
            return 1
        else:
            return -1
    def terminal(self):
        if (self.board[0][0] != 0 and self.board[1][0] != 0 and self.board[2][0] != 0) or (self.board[0][1] != 0 and self.board[1][1] != 0 and self.board[2][1] != 0) or (self.board[0][2] != 0 and self.board[1][2] != 0 and self.board[2][2] != 0):
            return 1
        if (self.board[0][0] != 0 and self.board[0][1] != 0 and self.board[0][2] != 0) or (self.board[1][0] != 0 and self.board[1][1] != 0 and self.board[1][2] != 0) or (self.board[2][0] != 0 and self.board[2][1] != 0 and self.board[2][2] != 0):
            return 1
        if (self.board[0][0] != 0 and self.board[1][1] != 0 and self.board[2][2] != 0) or (self.board[2][0] != 0 and self.board[1][1] != 0 and self.board[0][2] != 0):
            return 1
        for i in self.board:
            for j in self.board[i]:
                if j == 0:
                    return False
        
        return True
    # TODO: implement minimax and maximin
    def minimax(self):
        pass
    def maximin(self):
        pass
