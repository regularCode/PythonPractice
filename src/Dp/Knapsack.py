class Knapsack:

    def __init__(self, profits, weights, size):
        self.profits = profits
        self.weights = weights
        self.size = size

    def solve01knapsack(self):
        sack_size = self.size + 1
        item_count = len(self.weights)

        self.mem =  [[0 for x in range(sack_size)] for y in range(item_count +1)]

        for i in range(1, item_count+1):
            weigh = self.weights[i-1]
            for w in range(sack_size):
                if weigh <= w:
                    self.mem[i][w] = max(self.mem[i-1][w], self.mem[i-1][w - weigh] + self.profits[i-1])
                else:
                    self.mem[i][w] = self.mem[i-1][w]
        self.display()

    def display(self):
        j = 0
        for i in self.mem:
            print(j, i)
            j += 1
        print("\n----------------------\n")

    def findAnswer(self):
        temp = self.mem
        res = self.mem[-1][-1]
        w = self.size
        for i in range(len(self.weights), 0, -1):
            # weigh = self.weights[i]
            if res<=0:
                break; # answer foung
            if res == temp[i-1][w]:
                print("Same")
                continue
            else:
                print(f"Item {i} considered with weight {self.weights[i-1]} and profit {self.profits[i-1]}")
                print(w, res, i)
                res = res - self.profits[i-1]
                w = w - self.weights[i-1]


if __name__ == '__main__':
    weights = [2,3,4,5]
    profit = [1,2,5,6]
    size = 8

    knap = Knapsack(profit, weights, size)
    knap.solve01knapsack()
    knap.findAnswer()

