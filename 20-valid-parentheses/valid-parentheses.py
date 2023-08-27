class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for p in s:
            if p in ['{','(','[']:
                stack.append(p)
            else:
                if len(stack) == 0:
                    return False
                if stack[-1] + p not in ['()','[]','{}']:
                    return False
                stack.pop()
        
        return len(stack) == 0