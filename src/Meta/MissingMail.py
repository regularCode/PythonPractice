def display(dp):
    print("-------- Start")
    print (dp)
    print("--------End")


def getMaxExpectedProfit(N, V, C, S):
    # Write your code here
    maxProfit = 0
    dp = [0 for i in range(N + 1)]
    for i in range(N): # Coins
        commulative_profit = 0.0
        for j in range(i, N): # Days

            commulative_profit *= (1.0 - S)
            commulative_profit += V[j]

            dp[j + 1] = max(dp[j + 1],dp[i] + commulative_profit - C)

        maxProfit = max(dp[i+1], maxProfit)


if __name__ == '__main__':
    getMaxExpectedProfit(5, [10, 2, 8, 6, 4], 3, 0.5)


def icecreamParlor(m, arr):
    # Write your code here

    mem = {}

    for i, val in enumerate(arr):
        if val in mem:
            return (mem[val], i)
        mem[m - val] = i

