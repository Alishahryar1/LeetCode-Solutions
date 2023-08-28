# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def helper(self, prev, curr):
        if curr.next == None:
            curr.next = prev
            return curr
        temp = curr.next
        curr.next = prev
        return self.helper(curr, temp)
        

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        return self.helper(None, head)