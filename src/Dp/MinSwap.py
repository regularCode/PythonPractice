# Leetcode - 801

"""
Minimum Swaps To Make Sequences Increasing

You are given two integer arrays of the same length nums1 and nums2. In one operation, you are allowed to swap nums1[i] with nums2[i].

For example, if nums1 = [1,2,3,8], and nums2 = [5,6,7,4], you can swap the element at i = 3 to obtain nums1 = [1,2,3,4] and nums2 = [5,6,7,8].

Return the minimum number of needed operations to make nums1 and nums2 strictly increasing. The test cases are generated so that the given input always makes it possible.

An array arr is strictly increasing if and only if arr[0] < arr[1] < arr[2] < ... < arr[arr.length - 1].

"""
class Solution(object):
    def minSwap(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        self.n = len(nums1)

        def helperWithMem(indx, swap, mem):

            if indx >= self.n:
                return 0

            if mem[indx][swap] != -1:
                return mem[indx][swap]

            ans = float('inf')

            n1 = nums1[indx - 1] if indx > 0 else -1
            n2 = nums2[indx - 1] if indx > 0 else -1

            if swap == 1:
                n1, n2 = n2, n1

            if nums1[indx] > n1 and nums2[indx] > n2:
                ans = helperWithMem(indx + 1, 0, mem)
            if nums1[indx] > n2 and nums2[indx] > n1:
                ans = min(ans, 1 + helperWithMem(indx + 1, 1, mem))

            mem[indx][swap] = ans

            return ans

        mem = [[-1 for _ in range(2)] for _ in range(self.n + 1)]

        return helperWithMem(0, 0, mem)

    def minSwapTab(self, nums1, nums2):
        n = len(nums1)
        dp = [[0 for _ in range(2)] for _ in range(n + 1)]

        for indx in range (n-2, 0,-1):
            for swap in range(1, -1, -1):
                n1 = nums1[indx - 1] if indx > 0 else -1

                n2 = nums2[indx - 1] if indx > 0 else -1

                if swap == 1:
                    n1, n2 = n2, n1
                ans = float('inf')
                if nums1[indx] > n1 and nums2[indx] > n2:
                    ans = dp[indx + 1][0]
                if nums1[indx] > n2 and nums2[indx] > n1:
                    ans = min(ans, 1 + dp[indx + 1][1])

                dp[indx][swap] = ans
        return min(dp[1][0], 1+dp[1][1]) # +1 because of already swapped before beginning dp
