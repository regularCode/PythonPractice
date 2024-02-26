class Node:
    val = 0
    next_node = None

    def __repr__(self):
        print (self.val)

    def __init__(self, num):
        self.val = num