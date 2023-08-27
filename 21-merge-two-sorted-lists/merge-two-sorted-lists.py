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
        
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        a = list1
        b = list2
        if list1.val <= list2.val:
            head = list1
            a = a.next
            head.next = None
        else:
            head = list2
            b = b.next
            head.next = None
        
        curr = head
        while True:
            if a == None:
                curr.next = b
                break
            if b == None:
                curr.next = a
                break
            if a.val <= b.val:
                curr.next = a
                curr = curr.next
                a = a.next
            else:
                curr.next = b
                curr = curr.next
                b = b.next
            curr.next = None
        
        return head