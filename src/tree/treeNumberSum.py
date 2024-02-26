# leetcode - 129 Medium
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    num = []

    def helper(self, root, temp):
        if not root:
            return
        if not root.left and not root.right:
            return temp*10 + root.val
        nleft = self.helper(root.left, temp*10 + root.val)
        nright = self.helper(root.right, temp*10 + root.val)
        templeft = root.val * 10 + nleft
        tempright = root.val * 10 + nright
        return templeft + tempright

    def sumnumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        num = []
        temp = 0
        self.helper(root, temp)

