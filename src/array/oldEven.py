# Leetcode 2760
class Solution(object):
    def longestAlternatingSubarray(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        maxl = 0
        count = 0
        length = len(nums)
        i = 0
        while i < length:
            if (nums[i]%2 == 0 and nums[i] <= threshold) :
                count = 1
                i += 1
                while i < length and nums[i] % 2 != nums[i-1] %2 and nums[i] <= threshold:
                    count += 1
                    i += 1
                maxl = max(count, maxl)
            else:
                i += 1
        return maxl

if __name__ == "__main__":
    x = Solution()
    nums = [1, 1, 1, 2, 2, 3, 5, 7, 7, 7]
    result = x.longestAlternatingSubarray(nums, 5)
    print(result)