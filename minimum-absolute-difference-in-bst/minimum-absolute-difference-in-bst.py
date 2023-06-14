# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorder(self, root, traversal):
        if root.left:
            self.inorder(root.left, traversal)
        traversal.append(root.val)
        if root.right:
            self.inorder(root.right, traversal)
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        traversal = []
        self.inorder(root, traversal)

        absdiff_min = traversal[1] - traversal[0]
        for i in range(2, len(traversal)):
            absdiff_min = min(absdiff_min, traversal[i] - traversal[i - 1])
        return absdiff_min