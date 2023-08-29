# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def helper(self, root, targetSum, currSum):
        if root == None:
            return False
        if root.left == None and root.right == None:
            return currSum + root.val == targetSum
        elif root.left == None:
            return self.helper(root.right, targetSum, currSum + root.val)
        elif root.right == None:
            return self.helper(root.left, targetSum, currSum + root.val)
        else:
            return self.helper(root.right, targetSum, currSum + root.val) or self.helper(root.left, targetSum, currSum + root.val)
            
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        return self.helper(root, targetSum, 0)