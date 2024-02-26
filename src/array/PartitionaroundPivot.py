class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        values = []
        freq_pivot = 0
        newList = []
        for i in range(len(nums)):
            if nums[i] > pivot:
                values.append(nums[i])
            elif nums[i] == pivot:
                freq_pivot += 1
            else:
                newList.append(nums[i])

        for i in range(freq_pivot):
            newList.append(pivot)

        newList.extend(values)
        nums = newList
        return nums