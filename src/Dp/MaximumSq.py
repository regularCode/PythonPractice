class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        n = len(matrix)
        m = len(matrix[0])
        mem = [[0 for x in range(m)] for y in range(n)]
        self.display(matrix)
        out = 0
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    mem[i][j] = int(matrix[i][j])
                else:
                    if mem[i - 1][j - 1] > 0 and mem[i - 1][j] > 0 and mem[i][j - 1] > 0 and int(matrix[i][j]) == 1:
                        mem[i][j] = min(int(mem[i-1][j - 1]),
                                        int(mem[i - 1][j]),
                                        int(mem[i][j - 1])) + 1
                    else:
                        mem[i][j] = int(matrix[i][j])
                out = max(out, mem[i][j])
        self.display(mem)
        return out*out

    def display(self, mem):
        j = 0
        for i in mem:
            print(j, i)
            j += 1
        print("\n----------------------\n")


if __name__ == '__main__':
    matrix = [["0","0","0","0","0"],["0","0","0","0","0"],["0","0","0","0","1"],["0","0","0","0","0"]]
    S = Solution()
    print(S.maximalSquare(matrix))
