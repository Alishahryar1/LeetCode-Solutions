# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        current = head
        L = 0
        while (current != None):
            L += 1
            current = current.next
        current = head
        previous = None
        for i in range(L - n):
            previous = current
            current = current.next
        if current == head and current.next == None:
            return None
        elif current == head:
            head = head.next
            return head
        else:
            previous.next = current.next
        return head 