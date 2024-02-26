# Definition for singly-linked list.
class LinkedList(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def partition(self, head, x):
        if not head or not head.next:
            return head

        tempHead = LinkedList(-101)
        tempHead.next = head
        saveNewHead = tempHead
        prev = tempHead
        curr = tempHead.next

        buffer = LinkedList(-101)
        saveBuffer = buffer

        while curr:
            if curr.val >= x:
                prev.next = curr.next
                buffer.next = curr
                curr = curr.next
                buffer = buffer.next
                buffer.next = None
            else:
                prev = curr
                curr = curr.next

        prev.next = saveBuffer.next
        printlist(saveNewHead.next)


def printlist(head):
    temp = head
    values = []
    while temp:
        values.append(str(temp.val))
        temp = temp.next
    print (' -> '.join(values))


if __name__ == "__main__":
    n1 = LinkedList(1)
    n2 = LinkedList(4)
    n3 = LinkedList(3)
    n4 = LinkedList(2)
    n5 = LinkedList(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    head = n1
    printlist(head)
    s = Solution()
    s.partition(head, 3)



