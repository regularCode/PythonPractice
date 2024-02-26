class DoublyLinkedList:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.size = capacity
        self.m = {}
        self.head = DoublyLinkedList(-1, -1)
        self.tail = DoublyLinkedList(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def deleteNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def addNode(self, node):
        temp = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = temp
        temp.prev = node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.m:
            node = self.m[key]
            self.deleteNode(node)
            self.addNode(node)
            self.m[key] = self.head.next
            return self.head.next.val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # print("fetching")
        if key in self.m:
            # print(f"found {key}")
            node = self.m[key]
            node.val = value
            self.deleteNode(node)
            self.addNode(node)
            self.m[key] = self.head.next
        else:
            # print(f"not found {key}")
            if len(self.m) == self.size:
                prev = self.tail.prev
                self.deleteNode(prev)
                node = DoublyLinkedList(key, value)
                self.addNode(node)
                del self.m[prev.key]
                self.m[key] = node
            else:
                node = DoublyLinkedList(key, value)
                self.addNode(node)
                self.m[key] = node

    def __repr__(self):
        temp = self.head.next
        values = []
        while temp != self.tail:
            values.append(f"[{temp.key}, {temp.val}]")
            temp = temp.next
        values.append("None")
        return ' -> '.join(values)

    def printReverse(self):
        temp = self.tail.prev
        values = []
        while temp != self.head:
            values.append(f"[{temp.key}, {temp.val}]")
            temp = temp.prev
        values.append("None")
        return ' -> ' .join(values)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == "__main__":
    l = LRUCache(2)
    l.put(2, 1)
    l.put(2, 2)
    l.put(1, 1)
    l.get(2)
    print(l)
    l.put(4, 1)
    print(l)