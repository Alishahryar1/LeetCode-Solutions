# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def helper(self, root):
        if root == None:
            return -1
        leftHeight = self.helper(root.left)
        rightHeight = self.helper(root.right)
        self.balanced = False if (abs(leftHeight - rightHeight) > 1) else self.balanced
        return 1 + max(leftHeight, rightHeight)

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.balanced = True
        self.helper(root)
        return self.balanced