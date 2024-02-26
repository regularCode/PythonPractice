from Practice import Practice
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.stack.append((root, False))

    def next(self):
        """
        :rtype: int
        """
        found_next = False
        ret = 0
        while self.stack:
            print(self.stack)
            top, visited = self.stack.pop()
            if top:
                if not visited:
                    if top.right:
                        self.stack.append((top.right, False))
                    self.stack.append((top, True))
                    if top.left:
                        self.stack.append((top.left, False))
                else:
                    ret = int(top.val)
                    found_next = True
            if found_next:
                return ret

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if len(self.stack) > 0 else False


if __name__ == "__main__" :
    bt = Practice()

    root = bt.createBinaryTree()
    iterator = BSTIterator(root)
    while iterator.hasNext():
        print (iterator.next())


