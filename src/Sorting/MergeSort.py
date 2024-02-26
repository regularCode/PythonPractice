class MergeSort:

    def __init__(self, nums):
        self.nums = nums

    def sort(self):
        left = 0
        right = len(self.nums) - 1

        self.nums = self.mergeSort(self.nums, left, right)


    def merge(self, list1, list2):
        i,j=0,0
        result_list = []
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                result_list.append(list1[i])
                i+=1
            else:
                result_list.append(list2[j])
                j += 1
        while i < len(list1):
            result_list.append(list1[i])
            i += 1
        while j < len(list2):
            result_list.append(list2[j])
            j += 1

        print(list1, list2, result_list)

        return result_list

    def mergeSort(self, nums, left, right):
        if left < right:
            mid = (right + left)//2
            left_list = self.mergeSort(nums, left, mid)
            right_list = self.mergeSort(nums, mid + 1, right)
            self.mergeInplace(left, mid, right)
        return [nums[left]]

if __name__ == '__main__':
    list = [24,61,21,12,10,4,74,23]
    merge = MergeSort(list)
    merge.sort()
    print(merge.nums)
