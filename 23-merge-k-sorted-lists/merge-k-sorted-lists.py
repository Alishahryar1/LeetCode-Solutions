# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sort_key(self, ptr):
        return ptr.val
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        List = []
        for ptr in lists:
            while ptr != None:
                List.append(ptr)
                ptr = ptr.next
        List.sort(key = self.sort_key)
        
        if len(List) == 0:
            return None
        
        for i in range(len(List)):
            List[i - 1].next = List[i]
        List[-1].next = None
        return List[0]