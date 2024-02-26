class Solution(object):
    def max_so_farProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_so_far = nums[0]
        min_so_far = nums[0]
        res = 0

        for i in range(1, len(nums)):
            curr = nums[i]
            temp_max_so_far = max(curr, curr * max_so_far, curr * min_so_far)
            min_so_far = min(curr, curr * max_so_far, curr*min_so_far)

            max_so_far = temp_max_so_far
            res = max(max_so_far, res)

        return res