# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if not root:
            return 0
        closest = float('inf')

        while root:
            closest = min(closest, root.val, key=lambda x: (abs(target - x), x))
            if root.val > target:
                root = root.left
            else:
                root = root.right

        return closest

if __name__ == '__main__':
    s = Solution()

    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))

    print(s.closestValue(root, 3.14))