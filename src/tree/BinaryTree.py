class BinaryTree:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)

    def addLeft(self, Node):
        self.left = Node

    def addRight(self, Node):
        self.right = Node

