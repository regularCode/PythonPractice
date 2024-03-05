class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        m = n
        matrix = [[0 for _ in range(n)] for _ in range(n)]

        direction = 1
        row = 0
        col = -1
        count = 0
        while m * n > 0:
            for _ in range(n):
                col += direction
                count += 1
                matrix[row][col] = count

            m -= 1

            for _ in range(m):
                row += direction
                count += 1
                matrix[row][col] = count

            n -= 1
            direction *= -1

        return matrix