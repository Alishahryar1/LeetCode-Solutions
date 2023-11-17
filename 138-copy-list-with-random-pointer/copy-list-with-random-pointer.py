"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def insert(self, head, tail, node):
        if tail == None:
            head = tail = node
        else:
            tail.next = node
            tail = tail.next
        return head, tail

    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        curr = head
        while (curr != None):
            newNode = Node(curr.val)
            temp = curr.next
            curr.next = newNode
            newNode.next = temp
            curr = curr.next.next
        

        curr = head
        while (curr != None):
            curr.next.random = curr.random.next if (curr.random != None) else None
            curr = curr.next.next
        
        head1 = tail1 = None
        curr = head
        while (curr != None):
            node = curr.next
            curr.next = curr.next.next
            node.next = None
            head1, tail1 = self.insert(head1, tail1, node)
            curr = curr.next
        
        return head1    