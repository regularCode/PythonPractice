import heapq


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def findMid(head):
    if not head: return None

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def isPalindrome(sentence):

    lower = sentence.lower()

    st = ''
    for i in lower:
        if i.isalnum():
            st += i

    return st == st[::-1]

def findKthLargest(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    # with sorting
    heap = []
    for num in nums:
        print (heap)
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]

if __name__ == '__main__':
    print(findKthLargest([4,2,1,6,7,2,4,7,3,1], 3))