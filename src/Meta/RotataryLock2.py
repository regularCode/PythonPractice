def getMinCodeEntryTime(N, M, C):
    # Write your code here

    def minRotation(num, currentPosition):
        return min(abs(num - currentPosition), N - abs(num - currentPosition))

    def recur(p1, p2, sum_so_far, pos):
        if pos == M:
            return sum_so_far

        if p1 == p2:
            return recur(C[pos], p2, sum_so_far + minRotation(C[pos], p1), pos + 1)
        else:
            return min(recur(C[pos], p2, sum_so_far + minRotation(C[pos], p1), pos + 1),
                       recur(p1, C[pos], sum_so_far + minRotation(C[pos], p2), pos + 1))

    return recur(1, 1, 0, 0)

if __name__ == '__main__':
    print(getMinCodeEntryTime(10,4,[9,4,4,8]))