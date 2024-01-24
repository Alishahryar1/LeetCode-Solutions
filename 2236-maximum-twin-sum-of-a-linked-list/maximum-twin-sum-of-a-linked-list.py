# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        fast, slow = head.next, head
        while (fast and fast.next):
            fast = fast.next.next
            slow = slow.next

        list1, list2 = head, slow
        temp = list2
        list2 = list2.next
        temp.next = None
        prev, curr = None, list2
        
        while (curr):
            next = curr.next
            curr.next = prev
            prev, curr = curr, next
        
        list2 = prev
        maxSum = 0
        while (list2):
            maxSum = max(maxSum, list1.val + list2.val)
            list1 = list1.next
            list2 = list2.next

        return maxSum