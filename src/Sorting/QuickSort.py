class QuickSort:

    def __init__(self, nums):
        self.nums = nums

    def sort(self, left, right):
        if left < right:
            partition = self.partition(left, right)
            self.sort(left, partition)
            self.sort(partition + 1, right)



    def partition(self, left, right):
        leftSave = left
        pivot = self.nums[left]
        while left < right:
            while left < right and self.nums[left] <= pivot:
                # print(self.nums[left], right, left, pivot, self.nums)
                left += 1
            while self.nums[right] > pivot:
                right -= 1
            if left < right:
                self.nums[left], self.nums[right] = self.nums[right],self.nums[left]

        self.nums[leftSave], self.nums[right] = self.nums[right], self.nums[leftSave]

        return right

if __name__ == '__main__':
    list = [24,61,21,12,10,4,74,23]
    merge = QuickSort(list)
    print(f"Before sorting {merge.nums}")
    merge.sort(0, len(list) - 1)
    print(f"After sorting {merge.nums}")
