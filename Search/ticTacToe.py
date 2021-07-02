import math
import copy

X = "X"
O = "O"
EMPTY = 0

def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    x = 0
    o = 0
    for iIndex in range(len(board)):
        for j in board[iIndex]:
            if j == -1:
                o += 1
            if j == 1:
                x += 1
    if x > o:
        return -1
    else:
        return 1

def actions(board):
    out = []
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == 0:
                out.append((x, y))
    return out

def result(board, action):
    out = board
    if out[action[1]][action[0]] == 0:
        out[action[1]][action[0]] += player(board)
    else:
        raise Exception
    return out

def winner(board):
    if (board[0][0] == 1 and board[1][0] == 1 and board[2][0] == 1) or (board[0][1] == 1 and board[1][1] == 1 and board[2][1] == 1) or (board[0][2] == 1 and board[1][2] == 1 and board[2][2] == 1):
        return O
    if (board[0][0] == 1 and board[0][1] == 1 and board[0][2] == 1) or (board[1][0] == 1 and board[1][1] == 1 and board[1][2] == 1) or (board[2][0] == 1 and board[2][1] == 1 and board[2][2] == 1):
        return O
    if (board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1) or (board[2][0] == 1 and board[1][1] == 1 and board[0][2] == 1):
        return O
    if (board[0][0] == -1 and board[1][0] == -1 and board[2][0] == -1) or (board[0][1] == -1 and board[1][1] == -1 and board[2][1] == -1) or (board[0][2] == -1 and board[1][2] == -1 and board[2][2] == -1):
        return X
    if (board[0][0] == -1 and board[0][1] == -1 and board[0][2] == -1) or (board[1][0] == -1 and board[1][1] == -1 and board[1][2] == -1) or (board[2][0] == -1 and board[2][1] == -1 and board[2][2] == -1):
        return X
    if (board[0][0] == -1 and board[1][1] == -1 and board[2][2] == -1) or (board[2][0] == -1 and board[1][1] == -1 and board[0][2] == -1):
        return X
    return None

def terminal(board):
    if (board[0][0] == 1 and board[1][0] == 1 and board[2][0] == 1) or (board[0][1] == 1 and board[1][1] == 1 and board[2][1] == 1) or (board[0][2] == 1 and board[1][2] == 1 and board[2][2] == 1):
        return True
    if (board[0][0] == 1 and board[0][1] == 1 and board[0][2] == 1) or (board[1][0] == 1 and board[1][1] == 1 and board[1][2] == 1) or (board[2][0] == 1 and board[2][1] == 1 and board[2][2] == 1):
        return True
    if (board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1) or (board[2][0] == 1 and board[1][1] == 1 and board[0][2] == 1):
        return True
    if (board[0][0] == -1 and board[1][0] == -1 and board[2][0] == -1) or (board[0][1] == -1 and board[1][1] == -1 and board[2][1] == -1) or (board[0][2] == -1 and board[1][2] == -1 and board[2][2] == -1):
        return True
    if (board[0][0] == -1 and board[0][1] == -1 and board[0][2] == -1) or (board[1][0] == -1 and board[1][1] == -1 and board[1][2] == -1) or (board[2][0] == -1 and board[2][1] == -1 and board[2][2] == -1):
        return True
    if (board[0][0] == -1 and board[1][1] == -1 and board[2][2] == -1) or (board[2][0] == -1 and board[1][1] == -1 and board[0][2] == -1):
        return True
    for i in range(len(board)):
        for j in board[i]:
            if j == 0:
                return False
    return True

def utility(board):
    if winner(board) == O:
        return 1
    elif winner(board) == X:
        return -1
    else:
        return 0

# def minimax(board):
#     out = []
#     for action in actions(board):
#         out.append({'v': maxVal(result(board, action)), 'action': action})
#     out = max(out, key=lambda k: k['v'])

#     return out

# def maxVal(board):
#     print(board)
#     print(actions(board))
#     print(terminal(board))
#     print(utility(board))
#     if terminal(board):
#         return utility(board)
#     v = -1 * float('inf')
#     for action in actions(board):
#         newBoard = result(board, action)
#         v = max(v, minVal(newBoard))
#     return v

# def minVal(board):
#     print(board)
#     print(actions(board))
#     print(terminal(board))
#     print(utility(board))
#     if terminal(board):
#         return utility(board)
#     v = float('inf')
#     for action in actions(board):
#         newBoard = result(board, action)
#         v = min(v, maxVal(newBoard))
#     return v

def minimax(isMaxTurn, board, depth=1):
    if terminal(board):
        return {'v': utility(board)}
    places = []
    for action in actions(board):
        if not(action in places):
            places.append(action)
    
    # scores = [{'v': minimax(not isMaxTurn, result(board, action)), 'action': action} for action in places]
    # print(places)
    scores=[]
    for action in places:
        outBoard = result(board, action)
        minimaxOut = minimax(not isMaxTurn, outBoard, depth+1)
        scores.append({'v': minimaxOut['v'], 'action': action, 'depth': depth+1})
        board[action[1]][action[0]] = 0
    out = sorted(scores, key=lambda k: k['v'])
    # if player(board) == -1:
    #     out = reversed(out)
    out = sorted(out, key=lambda k: k['depth'])
    # print(out)
    if isMaxTurn:
        return out[-1]
    else:
        return out[0]

if __name__ == "__main__":
    board = initial_state()
    while True:
        print(player(board))
        if 1 != player(board):
            board = result(board, minimax(False, board)['action'])
        else:
            x=input()
            y=input()
            board = result(board, (int(x), int(y)))
        out = [str(row) for row in board]
        print('\n'.join(out))
        if terminal(board):
            print(utility(board))
            break