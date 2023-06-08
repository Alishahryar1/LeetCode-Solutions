# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def helper(self, root1, root2, root3):
        if root1 == root2 == None:
            return
        
        if root1 != None and root2 != None:
            root3.val = root1.val + root2.val
            
            if root1.left != None or root2.left != None:
                root3.left = TreeNode()
                self.helper(root1.left, root2.left, root3.left)
            
            if root1.right != None or root2.right != None:
                root3.right = TreeNode()
                self.helper(root1.right, root2.right, root3.right)
        
        elif root1 != None:
            root3.val = root1.val
            
            if root1.left != None:
                root3.left = TreeNode()
                self.helper(root1.left, root2, root3.left)
            
            if root1.right != None:
                root3.right = TreeNode()
                self.helper(root1.right, root2, root3.right)
        
        elif root2 != None:
            root3.val = root2.val
            if root2.left != None:
                root3.left = TreeNode()
                self.helper(root1, root2.left, root3.left)
            
            if root2.right != None:
                root3.right = TreeNode()
                self.helper(root1, root2.right, root3.right)

    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        root3 = None
        if root1 != None or root2 != None:
            root3 = TreeNode()
            self.helper(root1, root2, root3)
        return root3