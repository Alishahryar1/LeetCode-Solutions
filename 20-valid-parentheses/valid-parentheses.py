class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        left = ['(','[','{']
        complete = ['()','[]','{}']
        for p in s:
            if p in left:
                stack.append(p)
            else:
                if not stack or stack[-1] + p not in complete:
                    return False
                stack.pop()
        
        return not stack