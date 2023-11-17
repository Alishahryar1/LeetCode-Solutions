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
        heap = []
        for l in lists:
            if l:
                heapq.heappush(heap, (l.val, l))
        
        def insert(head, tail, node):
            if tail == None:
                head = tail = curr
            else:
                tail.next = curr
                tail = curr
            return head, tail
        
        head = tail = None
        while heap:
            val, curr = heapq.heappop(heap)
            if curr.next:
                heapq.heappush(heap, (curr.next.val, curr.next))
            curr.next = None
            head, tail = insert(head, tail, curr)
            
        return head