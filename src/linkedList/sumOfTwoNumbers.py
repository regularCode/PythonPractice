# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
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
            l1.val = sum%10
            carry  = sum // 10
            temp = l1
            l1 = l1.next
            l2 = l2.next

        while l2 is not None:
            temp.next = l2
            temp = l2
            t = l2.val
            temp.val = (t + carry) %10
            carry = (t + carry) // 10
            l2 = l2.next

        while l1 is not None:
            temp.next = l1
            temp = l1
            t = l1.val
            temp.val = (t + carry) %10
            carry = (t + carry) // 10
            #print (l1.val, carry)
            l1 = l1.next

        if carry == 1:
            temp.next = ListNode(carry)

        return result
