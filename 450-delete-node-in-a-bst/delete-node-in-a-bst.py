# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMin(self, root):
        curr = root
        while (curr != None and curr.left != None):
            curr = curr.left
        return curr.val

    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root == None:
            return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.left == None:
                return root.right
            elif root.right == None:
                return root.left
            else:
                rightMin = self.findMin(root.right)
                root.val = rightMin
                root.right = self.deleteNode(root.right, rightMin)
        return root