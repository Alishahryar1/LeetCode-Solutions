# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None
        temp = TreeNode(preorder[0])
        if len(preorder) == 1:
            return temp
        i = inorder.index(preorder[0])
        temp.left = self.buildTree(preorder[1: 1 + i], inorder[:i])
        temp.right = self.buildTree(preorder[1 + i:], inorder[i + 1:])
        return temp