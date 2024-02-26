class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


class CustomQueue:

    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        temp = self.head
        values = []
        while temp:
            values.append(str(temp.val))
            temp = temp.next
        return ' -> '.join(values) + ' -> None'

    def insert(self, node):
        if not self.tail:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def remove(self):
        if not self.head:
            return
        else:
            if self.head == self.tail:
                temp = self.head
                self.head = self.tail = None
                return temp
            else:
                temp = self.head
                self.head = self.head.next
                return temp

    def size(self):
        temp = self.head
        size = 0
        while temp:
            size += 1
            temp = temp.next
        return size

# if __name__ == '__main__':
#     queue = Queue()
#     queue.insert(Node(10))
#     queue.insert(Node(20))
#     print(queue)
#     print(queue.remove())
#     print(queue.remove())
#     print(queue.remove())
