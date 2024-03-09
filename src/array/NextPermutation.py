def nextPermutation(nums):

    N = len(nums)

    i = N - 2

    while i >= 0 and nums[i+1] <= nums[i]:
        i -= 1

    if i >= 0:
        j = N-1
        while j > i and nums[i] >= nums[j]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]

    j = N - 1
    i = i + 1

    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1

    print(nums)
    return nums




if __name__ == '__main__':
    nextPermutation([4,2,3,1])