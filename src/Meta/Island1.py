class Solution(object):
    def numIslands(self, board):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        row = len(board)
        col = len(board[0])
        stack = []
        # mem = [[False for _ in range(len(board[0]))] for _ in range(len(board)) ]
        resp = []

        row_offset = [1, 0, -1, 0]
        col_offset = [0, 1, 0, -1]
        sum = 0

        for i in range(row):
            for j in range(col):
                if board[i][j] == 1:
                    path = []
                    stack.append((i, j))
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

        return len(resp)