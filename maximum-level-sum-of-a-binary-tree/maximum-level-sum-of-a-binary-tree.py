# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [(1, root)]
        max_level_sum = root.val
        level_sum = 0
        max_level = 1
        while len(queue) > 0:
            level, current = queue[0]
            level_sum += current.val
            del queue[0]
            if current.left:
                queue.append((level + 1, current.left))
            if current.right:
                queue.append((level + 1, current.right))
            if len(queue) == 0:
                if level_sum > max_level_sum:
                    max_level = level
                    max_level_sum = level_sum
            elif queue[0][0] > level:
                if level_sum > max_level_sum:
                    max_level = level
                    max_level_sum = level_sum
                level_sum = 0
        return max_level