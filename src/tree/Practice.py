from BinaryTree import BinaryTree

class Practice:
    def createBinaryTree(self):
        bt = BinaryTree(10,
                        BinaryTree(20,
                                   BinaryTree(13),
                                   BinaryTree(12,
                                              BinaryTree(11,
                                                         BinaryTree(12),
                                                         BinaryTree(22)),
                      BinaryTree(21))), BinaryTree(7))
        return bt

    def inOrderTraveralRecursive(self, root):
        if not root: return ' '
        return self.inOrderTraveralRecursive(root.left) + str(root.val) + self.inOrderTraveralRecursive(root.right)

    def inOrderUsingStack(self, root):
        if not root: return ' '
        stack = []
        stack.append((root, False))
        res = []
        while stack:
            top, visited = stack.pop()
            if top:
                if not visited:
                    if top.right:
                        stack.append((top.right, False))
                    stack.append((str(top.val), True))
                    if top.left:
                        stack.append((top.left, False))
                else:
                    res.append(top)

        return ' '.join(res)

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root: return ' '
        if not root.right and not root.left: return root

        leftTrail = self.flatten(root.left)
        rightTrail = self.flatten(root.right)

        if leftTrail:
            leftTrail.right = root.right
            root.right = leftTrail.left
            leftTrail.left = None

        return rightTrail if rightTrail else leftTrail

if __name__ == "__main__" :
    s = Practice()
    root = s.createBinaryTree()

    print(s.inOrderTraveralRecursive(root))
    print(s.inOrderUsingStack(root))
    s.flatten(root)
    print (s.inOrderUsingStack(root))