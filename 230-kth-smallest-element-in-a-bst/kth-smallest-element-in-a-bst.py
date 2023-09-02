# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def helper(self, root, List):
        if root == None:
            return
        self.helper(root.left, List)
        List.append(root.val)
        self.helper(root.right, List)

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        List = []
        self.helper(root, List)
        return List[k - 1]