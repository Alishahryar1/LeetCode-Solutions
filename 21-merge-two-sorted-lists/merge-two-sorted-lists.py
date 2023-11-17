# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertAtTail(self, head, tail, node):
        if head == tail == None:
            head = tail = node
            return head, tail

        tail.next = node
        tail = node
        return head, tail
    
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ptr1, ptr2 = list1, list2
        head = tail = None
        while ptr1 and ptr2:
            if ptr1.val < ptr2.val:
                node = ptr1
                ptr1 = ptr1.next
            else:
                node = ptr2
                ptr2 = ptr2.next
            head, tail = self.insertAtTail(head, tail, node)
            
        head, tail = self.insertAtTail(head, tail, ptr1) if (ptr1) else self.insertAtTail(head, tail, ptr2)
        
        return head