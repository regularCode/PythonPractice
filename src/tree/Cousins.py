# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """

        def findParent(root, node, level=0):
            if not root:
                return

            if root.left == node or root.right == node:
                return root, level

            left = findParent(root.left, node, level + 1)
            return left if left else findParent(root.right, node, level + 1)

        xparent, xlevel = findParent(root, x, 0)
        yparent, ylevel = findParent(root, y, 0)

