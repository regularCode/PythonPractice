import collections


def display(grid):
    print("---------------")
    for i in grid:
        print(i)
    print("---------------")

def shortestPathBinaryMatrix(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    n = len(grid)
    que = collections.deque()

    que.append((0, 0))

    grid[0][0] = -1
    row_offset = [1, -1, 0, 0, -1, -1, 1, 1]
    col_offset = [0, 0, -1, 1, -1, 1, 1, -1]

    while que:
        levelSize = len(que)
        for i in range(levelSize):
            display(grid)
            r, c = que.popleft()

            for offset_r, offset_c in zip(row_offset, col_offset):
                new_r = r + offset_r
                new_c = c + offset_c

                if 0 <= new_r < n and 0 <= new_c < n:
                    if grid[new_r][new_c] == 1:
                        continue
                    if grid[new_r][new_c] == 0:
                        grid[new_r][new_c] = grid[r][c] - 1
                        que.append((new_r, new_c))
                    elif grid[new_r][new_c] < grid[r][c] - 1:
                        grid[new_r][new_c] = grid[r][c] - 1
                        que.append((new_r, new_c))

    return grid[n - 1][n - 1] * -1


if __name__ == '__main__':
    grid = [[0,0,0],[1,1,0],[1,1,0]]
    shortestPathBinaryMatrix(grid)