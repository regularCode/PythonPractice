def findMissingRanges(nums, lower, upper):
    """
    :type nums: List[int]
    :type lower: int
    :type upper: int
    :rtype: List[List[int]]
    """
    ans = []
    nums.append(upper + 1)
    print(nums)

    for i in range(1, len(nums)):
        if nums[i] > lower and abs(nums[i] - nums[i - 1]) > 1:
            ra = [max(nums[i - 1] + 1, lower), min(nums[i] - 1, upper)]
            ans.append(ra)
    print(ans)
    return ans

if __name__ == '__main__':
    findMissingRanges([0,1,3,50,75],0, 99)