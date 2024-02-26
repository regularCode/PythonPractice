class DoublyLinkedList:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.size = capacity
        self.m = {}
        self.c = {}
        self.head = DoublyLinkedList(-1, -1)
        self.tail = DoublyLinkedList(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def deleteNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.c[node.key]

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
            count = self.c[key]
            self.deleteNode(node)
            self.addNode(node)
            self.m[key] = self.head.next
            self.c[key] = count + 1
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
            count = self.c[key]
            node.val = value
            self.deleteNode(node)
            self.addNode(node)
            self.m[key] = self.head.next
            self.c[key] = count + 1
        else:
            # print(f"not found {key}")
            if len(self.m) == self.size:
                headc = self.c[self.head.next.key]
                tailc = self.c[self.tail.prev.key]
                todel = None
                if headc >= tailc:
                    todel = self.m[self.tail.prev.key]
                else:
                    todel = self.m[self.head.next.key]
                prev = todel
                self.deleteNode(prev)
                node = DoublyLinkedList(key, value)
                self.addNode(node)
                del self.m[todel.key]
                self.m[key] = node
                self.c[key] = 1
            else:
                node = DoublyLinkedList(key, value)
                self.addNode(node)
                self.m[key] = node
                self.c[key] = 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == "__main__":
    l = LFUCache(2)
    l.put(1, 1)
    l.put(2, 2)
    l.get(1)
    l.put(3, 3)
    l.get(2)
    l.get(3)
    l.put(4, 4)
    l.get(1)
    l.get(3)
    l.get(4)