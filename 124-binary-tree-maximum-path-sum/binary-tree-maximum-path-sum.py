# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.max_sum = float('-inf')
    
    def helper(self, root):
        if root.left == None and root.right == None:
            self.max_sum = max(self.max_sum, root.val)
            return root.val
        
        if root.left != None and root.right != None:
            left_sum = self.helper(root.left)
            right_sum = self.helper(root.right)
            self.max_sum = max(self.max_sum, root.val + left_sum + right_sum, root.val, root.val + left_sum, root.val + right_sum)
            return max(root.val + left_sum, root.val + right_sum, root.val)
        
        elif root.right != None:
            right_sum = self.helper(root.right)
            self.max_sum = max(self.max_sum, root.val + right_sum, root.val)
            return max(root.val + right_sum, root.val)
        
        elif root.left != None:
            left_sum = self.helper(root.left)
            self.max_sum = max(self.max_sum, root.val + left_sum, root.val)
            return max(root.val + left_sum, root.val)

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.helper(root)
        return self.max_sum