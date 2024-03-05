# Given input data of a geographic map, as a matrix where 0s represent water and 1s represent land, return the number of islands.

# 0 1 1 0 1 0 1
# 0 1 0 0 1 0 1
# 0 1 0 0 1 1 1
# 1 0 0 0 0 0 0

# No diagonals only horizontal and verticals

# 1. Iterate over 2D array
# 2. Find first 1
# 3. Do a DFS/BFS from that point to all neighboring 1's and track them using a memory
# 4. Once stack is empty or dfs is complete. Increament the island count.

def display(list_of_list):
    print("--------")
    for i in list_of_list:
        print(i)
    print("--------")





def islandCount(board):
    def computeWater(r, c):
        count = 0
        for k in range(4):
            n_r, n_c = r + row_offset[k], c + col_offset[k]
            if 0 <= n_r < row and 0 <= n_c < col:
                if board[n_r][n_c] == 0:
                    count += 1
            else:
                count += 1
        print (count)
        return count

    row = len(board)
    col = len(board[0])
    stack = []
    # mem = [[False for _ in range(len(board[0]))] for _ in range(len(board)) ]
    resp = []

    display(board)

    row_offset = [1, 0, -1, 0]
    col_offset = [0, 1, 0, -1]
    sum = 0

    for i in range(row):
        for j in range(col):
            if board[i][j] == 1:
                path = []
                stack.append((i, j))
                # mem[i][j] = True
                board[i][j] *= -1
                path.append((i, j))
                while stack:
                    r, c = stack.pop()
                    sum += computeWater(r, c)
                    for k in range(4):
                        n_r, n_c = r + row_offset[k], c + col_offset[k]
                        if 0 <= n_r < row and 0 <= n_c < col and board[n_r][n_c] == 1:
                            stack.append((n_r, n_c))
                            # mem[n_r][n_c] = True
                            path.append((n_r, n_c))
                            board[n_r][n_c] *= -1
                resp.append(path)
                print("Island - ", path)

    # display(board)
    # display(mem)
    # print(resp)
    print(sum)

if __name__ == '__main__':
    board = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]

    islandCount(board)