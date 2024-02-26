from CustomQueue import CustomQueue, Node

class StackUsingQueue:

    def __init__(self):
        self.queue1 = CustomQueue()
        self.queue2 = CustomQueue()

    def push(self, val):
        if self.queue2.size() > 0:
            for i in range(self.queue2.size()):
                self.queue1.insert(self.queue2.remove())

        self.queue1.insert(Node(val))

    def pop(self):
        if self.queue1.size() > 0:
            for i in range(self.queue1.size()):
                self.queue2.insert(self.queue1.remove())

        if self.queue2.size() > 0:
            return self.queue2.remove()
        else:
            return "no element"


if __name__ == '__main__':
    stack = StackUsingQueue()
    print(stack.pop())
    stack.push(1)
    stack.push(2)
    print(stack.pop())
    stack.push(3)
    print(stack.pop())
    stack.push(4)
    print(stack.pop())
    print(stack.pop())

