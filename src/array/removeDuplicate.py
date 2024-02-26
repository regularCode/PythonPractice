# Leetcode 26
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p = 0
        for i in range(1, len(nums)):
            if nums[p] != nums[i]:
                p += 1
                nums[p] = nums[i]

        return p + 1

    def __init__(self):
        print("Welcome to Solution class")


if __name__ == "__main__":
    x = Solution()
    nums = [1, 1, 2, 2, 3, 5, 7, 7]
    result = x.removeDuplicates(nums)
    print (nums[0:result])

