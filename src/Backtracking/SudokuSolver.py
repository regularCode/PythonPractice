def isBoardSafe(board, num, r, c):

    # print("Rows - ")
    for i in range(9):
        # print (r, i)
        if board[r][i] == num:
            return False

    # print("Col - ")
    for j in range(9):
        # print(j, c)
        if board[j][c] == num:
            return False

    pos_x = r - r%3
    pos_y = c - c%3

    # print("Box - ")
    for i in range(pos_x, pos_x + 3):
        for j in range(pos_y, pos_y + 3):
            # print (pos+ i, pos+j)
            if board[i][j] == num:
                return False

    return True


def findFreeSlot(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i,j

    return -1, -1


def backtrack(board):
    display(board)
    r,c = findFreeSlot(board)

    if r == -1 and c == -1:
        return True

    for i in range (1,10):
        if isBoardSafe(board, i, r, c):
            board[r][c] = i
            if backtrack(board):
                return True
            else:
                board[r][c] = 0

    return False

def display(board):

    print("---------------")
    for i in board:
        print(i)
    print("---------------")

if __name__ == '__main__':
    board = [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]
    ]

    print(backtrack(board))
    display(board)