# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        
        queue = [root]
        output = []
        while (len(queue) > 0):
            output.append(queue[0].val)
            for _ in range(len(queue)):
                curr = queue.pop(0)
                if curr.right:
                    queue.append(curr.right)
                if curr.left:
                    queue.append(curr.left)
            
        return output