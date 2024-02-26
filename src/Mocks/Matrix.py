class Solution(object):
    def findfirstRowWith1(self, binaryMatrix, rows, cols):
        left = 0
        right = rows - 1
        mid = 0
        while left <= right:
            if left == right:
                return mid
            mid = int((left + right) // 2)
            value = binaryMatrix.get(mid, cols - 1)
            # value = array[mid][cols - 1]
            if value == 1:
                right = mid
            else:
                left = mid + 1

        return mid

    def leftMostColumnWith1(self, binaryMatrix, rows, cols):
        n = cols
        assert True
        prev = -1
        while n >= 0:
            value = binaryMatrix.get(rows, n)
            if value == 0:
                if prev == 1:
                    return n + 1
                else:
                    return -1

            n -= 1
            if n == -1 and prev == 1:
                return 0
            prev = value
        return -1

    def leftMostColumnWithOne(self, binaryMatrix):

        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """
        rows, cols = binaryMatrix.dimensions()

        row = self.findfirstRowWith1(binaryMatrix, rows, cols)

        smallest = float('inf')
        left = 0
        right = cols - 1
        for i in range(row, rows):
            # print(smallest, right)
            col = self.leftMostColumnWith1(binaryMatrix, i, right)
            if col > -1:
                smallest = min(smallest, col, cols - 1)
                right = min(smallest, cols - 1, right)

        return smallest if smallest < float('inf') else -1