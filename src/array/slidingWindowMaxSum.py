class Solution:
    def slidingWindowMaxSum(self, nums, k):
        """
        :param nums: List<int>
        :param k: int
        :return: List<List>
        """
        sum = 0
        ap = []
        for i in range(len(nums)):
            if i > k:
                ap.append(sum)
                sum += nums[i] - nums[i-k-1]
            else:
                sum += nums[i]
        ap.append(sum)
        return ap

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        s = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in s:
                return [s[num], i]
            if num > 0:
                if num > target:
                    s[num - target] = i
                else:
                    s[target - num] = i
            else:
                s[target - num] = i
            print (s)
        return False

if __name__ == "__main__":
    s = Solution()
    nums = [-1,-3,-2, -5, -6, -7]
    # print(s.slidingWindowMaxSum(nums, 2))
    print(s.twoSum(nums, -8))

