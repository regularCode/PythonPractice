class MyQueue(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack1.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if self.stack2: return self.stack2.pop()
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        if self.stack2:
            return self.stack2.pop()
        else:
            return -1

    def peek(self):
        """
        :rtype: int
        """
        if self.stack2: return self.stack2[-1]
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        if self.stack2:
            return self.stack2[-1]
        else:
            return -1

    def empty(self):
        """
        :rtype: bool
        """
        if self.stack2 is not None or self.stack1 is not None:
            return False
        return True

# Your MyQueue object will be instantiated and called as such:
if __name__ == '__main__':
    obj = MyQueue()
    obj.push(10)
    print(obj.pop())
    print(obj.peek())
    print(obj.empty())