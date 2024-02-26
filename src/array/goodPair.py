# Leetcode 1512
class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        sum = 0
        for i in nums:
            if dict.__contains__(i):
                dict[i] = dict.__getitem__(i) + 1
            else:
                dict[i] = 1
        print (dict)

        for k,v in dict.items():
            if v >= 2:
                sum = sum + self.fact(v)/v
        return sum

    def fact(self, num: int) -> int :
        fc = 1
        for i in range(1,num+1):
            fc *= i
        return fc

    def __init__(self):
        print("Welcome to Solution class")


if __name__ == "__main__":
    x = Solution()
    nums = [1, 1, 1, 1, 2, 2, 7 , 7]
    result = x.numIdenticalPairs(nums)
    print (result)