# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = []
        num2 = []
        
        current = l1
        while current != None:
            num1.append(current.val)
            current = current.next
        
        current = l2
        while current != None:
            num2.append(current.val)
            current = current.next
        
        a = 0
        b = 0
        
        for i in range(len(num1)):
            a += num1[i] * (10 ** i)
        
        for i in range(len(num2)):
            b += num2[i] * (10 ** i)
            
        c = a + b
        num3 = []
        while c > 0:
            num3.append(c%10)
            c = c // 10
        
        l3 = ListNode()
        current = l3
        for i in range(len(num3)):
            current.val = num3[i]
            if i == len(num3) - 1:
                break
            current.next = ListNode()
            current = current.next
        
        return l3