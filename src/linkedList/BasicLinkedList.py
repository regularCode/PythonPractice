from random import randint

from Node import Node


class LinkedList:
    head = None

    def __init__(self):
        self.head = None

    def add(self, num):
        new_node = Node(num)
        new_node.next_node = self.head
        self.head = new_node

    def printList(self):
        stringBuilder = []
        temp = self.head
        while temp is not None:
            stringBuilder.append(str(temp.val))
            temp = temp.next_node
            if temp is not None:
                stringBuilder.append("->")
            else:
                stringBuilder.append(" -> None")
        return ' '.join(stringBuilder)

    def __repr__(self):
        return self.printList()

    def search(self, key):
        temp = self.head
        i = 0
        while temp is not None:
            if temp.val == key:
                print(f"Number {key} found at index {i}")
                break
            i += 1
            temp = temp.next_node

    def insertBefore(self, num, key):
        if self.head is None:
            print ("No value in Linked List")
            return
        temp = self.head
        pre = None
        n = Node(num)
        while temp is not None:
            if temp.val == key:
                if pre is None:
                    n.next_node = temp
                    self.head = n
                    print (f"Inserting {num} in the begining")
                    return
                else:
                    pre.next_node = n
                    n.next_node = temp
                    print (f"Inserting {num} somewhere inside")
                    return
            else:
                pre = temp
                temp = temp.next_node
        print(f"Can't find key {key} to insert number {num} before")

    def insertAfter(self, num, key):
        if self.head is None:
            print ("No value in Linked List")
            return
        temp = self.head
        n = Node(num)
        while temp is not None:
            if temp.val == key:
                n.next_node = temp.next_node
                temp.next_node = n
                return
            else:
                temp = temp.next_node
        print (f"Can't find key {key} to insert {num}")

    def pairwiseSwap(self):
        if self.head is None or self.head.next_node is None:
            print("Nothing to swap returning")
            return
        temp = Node(0)
        temp.next_node = self.head
        curr = temp

        while curr.next_node is not None and curr.next_node.next_node is not None:
            # find two numbers
            n1 = curr.next_node
            n2 = curr.next_node.next_node

            # Swap
            n1.next_node = n2.next_node
            n2.next_node = n1

            # ready for next
            curr.next_node = n2
            curr = n1

        self.head = temp.next_node

    def addTwoNumbers(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1 is None and l2 is None:
            return None

        result = l1
        temp = l1
        carry = 0
        while l1 is not None and l2 is not None:
            sum = l1.val + l2.val + carry
            l1.val = sum % 10
            carry = sum // 10
            temp = l1
            l1 = l1.next
            l2 = l2.next

        while l2 is not None:
            temp.val = (temp.val + carry) % 10
            carry = (temp.val + carry) // 10
            temp = temp.next
            l2 = l2.next

        while l1 is not None:
            temp.val = (temp.val + carry) % 10
            carry = (temp.val + carry) // 10
            temp = temp.next
            l1 = l1.next

        return result
if __name__ == "__main__":
    l1 = LinkedList()
    for i in range(10):
        l1.add(randint(1, 9))
    l2 = LinkedList()
    for i in range(5):
        l2.add(randint(1, 9))
    l1.printList()
    l2.printList()
    LinkedList.addTwoNumbers(l1.head, l2.head)

