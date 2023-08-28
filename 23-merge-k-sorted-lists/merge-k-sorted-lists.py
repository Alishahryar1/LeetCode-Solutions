# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        L = 0
        for ptr in lists:
            while (ptr != None):
                L += 1
                ptr = ptr.next
        
        tail = None
        head = None
        for i in range(L):
            val_min = float('inf')
            i_min = -1
            for i, ptr in enumerate(lists):
                if ptr == None:
                    continue
                if ptr.val <= val_min:
                    val_min = ptr.val
                    i_min = i
            if tail == None:
                head = lists[i_min]
                tail = head
                lists[i_min] = lists[i_min].next
                tail.next = None
            else:
                tail.next = lists[i_min]
                lists[i_min] = lists[i_min].next
                tail.next.next = None
                tail = tail.next
        
        return head