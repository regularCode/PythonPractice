from typing import List

class Node:
    def __init__(self, start: int, end: int) -> None:
        self.left = None
        self.right = None
        self.total = 0
        self.start = start
        self.end = end

    def __repr__(self):
        if self.left or self.right:
            return f"[{self.left}:{self.right} {self.start}:{self.end}  - {self.total}]"
        return f"[{self.start}:{self.end}  - {self.total}]"


class SegmentTree:

    def __init__(self, nums: List[int]) -> None:
        def createSegmentTree(nums:List[int], start: int, end: int) -> Node:

            if start == end: # Leaf node
                node = Node(start, end)
                node.total = nums[start]
                return node

            if start > end:
                return None

            mid = (start + end)//2
            root = Node(start, end)

            root.left = createSegmentTree(nums, start, mid)
            root.right = createSegmentTree(nums, mid+1, end)

            root.total = root.left.total + root.right.total

            return root

        self.root = createSegmentTree(nums, 0, len(nums) - 1)

    def __repr__(self):
        return f"{self.root}"

    def rangeSum(self, i, j):

        def helper(root:Node, i:int, j:int) -> int:

            if i == root.start and j == root.end:
                return root.total

            mid = (root.start + root.end)//2

            if mid >= j:
                return helper(root.left, i, j)
            elif mid+1 <= i:
                return helper(root.right, i, j)
            else:
                return helper(root.left, i, mid) + helper(root.right, mid+1, j)

        return helper(self.root, i, j)

    def update(self, index, val):

        def helper(root, index, val):

            if root.start == root.end:
                root.total = val
                return val

            mid = (root.start + root.end)//2

            if index <= mid:
                helper(root.left, index, val)
            else:
                helper(root.right, index, val)

            root.total = root.left.total + root.right.total

            return root.total

        return helper(self.root, index, val)

if __name__ == '__main__':
    segment = SegmentTree([1,2,3,4,5,6,7,8])
    print(segment.rangeSum(0,7))
    print(segment.update(2,43))
    print(segment.rangeSum(0,7))
    print(segment)
    sum = segment.rangeSum(0,8)
    print(f"Avg for range 0-7 is {sum}", sum/8)

