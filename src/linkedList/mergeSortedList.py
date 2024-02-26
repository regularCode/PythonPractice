# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result = None
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val < list2.val:
            result = list1
            list1 = list1.next
        else:
            result = list2
            list2 = list2.next

        output = result

        while list1 and list2:
            if list1.val < list2.val:
                output.next = list1
                output = list1
                list1 = list1.next
            else:
                output.next = list2
                output = list2
                list2 = list2.next

        if list1:
            output.next = list1

        if list2:
            output.next = list2

        return result
