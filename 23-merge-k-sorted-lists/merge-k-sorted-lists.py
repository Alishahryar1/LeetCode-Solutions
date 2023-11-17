# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insert(self, head, tail, node):
        if tail == None:
            head = tail = node
        else:
            tail.next = node
            tail = node
        return head, tail
    
    def merge(self, list1, list2):
        ptr1, ptr2 = list1, list2
        head = tail = None
        while (ptr1 and ptr2):
            if ptr1.val < ptr2.val:
                node = ptr1
                ptr1 = ptr1.next
            else:
                node = ptr2
                ptr2 = ptr2.next
            node.next = None
            head, tail = self.insert(head, tail, node)
        
        head, tail = self.insert(head, tail, ptr1) if ptr1 else self.insert(head, tail, ptr2)
        return head
    
    def helper(self, L, R, lists):
        if L == R or len(lists) == 0:
            return lists[L]
        m = (L + R)//2
        left = self.helper(L, m, lists)
        right = self.helper(m + 1, R, lists)
        return self.merge(left, right)

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        return self.helper(0, len(lists) - 1, lists)
        