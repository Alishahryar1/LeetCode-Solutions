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

    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head == None:
            return head
        fast = slow = head
        while (fast.next and fast.next.next):
            slow = slow.next
            fast = fast.next.next
        nextNode = slow.next
        slow.next = None
        slow = nextNode

        prev, curr = None, nextNode
        while (curr != None):
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        
        head1 = tail1 = None
        ptr1, ptr2 = head, prev
        while (ptr1 and ptr2):
            node = ptr1
            ptr1 = ptr1.next
            node.next = None
            head1, tail1 = self.insert(head1, tail1, node)
            node = ptr2
            ptr2 = ptr2.next
            node.next = None
            head1, tail1 = self.insert(head1, tail1, node)
            
        head1, tail1 = self.insert(head1, tail1, ptr1) if (ptr1) else self.insert(head1, tail1, ptr2)

        return head1

        