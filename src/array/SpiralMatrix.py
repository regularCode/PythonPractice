class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        n = len(matrix[0])

        direction = 1
        row = 0
        col = -1
        res = []
        while m * n > 0:
            for _ in range(n):
                col += direction
                res.append(matrix[row][col])

            m -= 1

            for _ in range(m):
                row += direction
                res.append(matrix[row][col])

            n -= 1
            direction *= -1

        return res