class Solution:
    def combinationSum3(self, k, n):
        self.output = []

        def helper(start, temp, target, li):
            if temp == 0 and target == 0:
                self.output.append(li[:])
                return
            if start > 9 or temp < 0:
                return
            for i in range(start, 10):
                if target - i >= 0:
                    li.append(i)
                    helper(i + 1, temp - 1, target - i, li)
                    li.pop()

        helper(1, k, n, [])
        print(self.output)

if __name__ == '__main__':
    Solution().combinationSum3(2, 11)