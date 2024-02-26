def display(array2D):
    j = 0
    for i in array2D:
        print(j, i)
        j+=1
    print("-----------------\n")



def EditDistnace(source, destination):

    m = len(source)
    n = len(destination)

    dp = [[0 for x in range(n+1)] for y in range(m+1)]
    display(dp)
    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif source[i-1] == destination[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

        display(dp)


if __name__ == '__main__':
    source = "abcdef"
    destination = "acbef"
    EditDistnace(source, destination)
    EditDistnace(destination, source)