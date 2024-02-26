# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 141

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next: return False
        slow = head
        fast = head.next

        while slow != fast:
            # print (slow.val, fast.val)
            slow = slow.next
            if fast and fast.next:
                fast = fast.next.next
            else:
                return False

        # print (slow.val, fast.val)
        return True
