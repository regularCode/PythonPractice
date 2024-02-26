class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum = 0
        for num in nums:
            set_bit = self.fetch_set_bit(num)
            print (num, set_bit)
            if set_bit == k:
                print (f"adding {num}")
                sum += num
        return sum

    def fetch_set_bit(self, num):
        count = 0
        temp = num
        while temp > 0:
            count += temp & 1
            temp = temp >> 1
        return count


if __name__ == "__main__":
    nums = [5, 10, 1, 5, 2]

    s = Solution()

    s.sumIndicesWithKSetBits(nums, 1)
