import abc
from abc import ABCMeta, abstractmethod

"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""


class Node:
    __metaclass__ = ABCMeta

    # define your fields here
    @abstractmethod
    def evaluate(self):
        pass

class TreeNode(Node):

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def evaluate(self):
        eval_left = self.evaluateSubTree(self.left)
        eval_right = self.evaluateSubTree(self.right)
        return self.compute(self.val, eval_left, eval_right)


    def evaluateSubTree(self, node):
        if node.val.isdigit():
            return int(node.val)
        eval_left = self.evaluateSubTree(node.left)
        eval_right = self.evaluateSubTree(node.right)
        return self.compute(node.val, eval_left, eval_right)

    def compute(self, operator, eval_left, eval_right):
        if operator == '+':
            return int(eval_right) + int(eval_left)
        if operator == '-':
            return int(eval_left) - int(eval_right)
        if operator == '*':
            return int(eval_left) * int(eval_right)
        if operator == '/':
            return int(eval_left) / int(eval_right)


"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree representing it as a Node.
"""


class TreeBuilder(object):
    def buildTree(self, postfix):
        """
        :type s: List[str]
        :rtype: Node
        """
        s = []
        for i in postfix:
            if i.isdigit():
                s.append(TreeNode(i))
            else:
                right = s.pop()
                left = s.pop()
                s.append(TreeNode(i, left, right))
        return s.pop()


"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""

if __name__ == '__main__':
    postfix = ["3","4","+","2","*","7","/"]
    obj = TreeBuilder();
    expTree = obj.buildTree(postfix)
    ans = expTree.evaluate()