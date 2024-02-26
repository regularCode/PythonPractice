import collections


class HeapSort:

    def __init__(self, nums):
        self.nums = collections.defaultdict

    def heapify(self):
        n = len(self.nums)
        for i in range(n//2 + 1, -1, -1):
            # print(i)
            self.pushDown(i, n)

    def pushDown(self, i, n):
        left = 2*i + 1
        right = 2*i + 2

        if left < n and self.nums[left] > self.nums[i]:
            self.nums[left], self.nums[i] = self.nums[i], self.nums[left]
            self.pushDown(left, n)

        if right < n and self.nums[right] > self.nums[i]:
            self.nums[right], self.nums[i] = self.nums[i], self.nums[right]
            self.pushDown(right, n)

    def __repr__(self):
        return str(self.nums)

    def removeTopElement(self):
        top = self.nums[0]
        n = len(nums) - 1
        last = self.nums[n]
        self.nums[0] = last
        self.pushDown(0, n - 1)
        nums[last] = top

    def sort(self):
        n = len(self.nums)
        for i in range(n - 1, -1, -1):
            top = self.nums[0]
            last = self.nums[i]
            self.nums[0] = last
            self.pushDown(0, i)
            nums[i] = top

    def hasNext(self):
        return len(self.nums) > 0

if __name__ == '__main__':
    nums = [10, 20, 15, 12, 40, 25, 18]
    heap = HeapSort(nums)
    print(heap)
    heap.heapify()
    print(heap)
    heap.sort()
    print(heap.nums)