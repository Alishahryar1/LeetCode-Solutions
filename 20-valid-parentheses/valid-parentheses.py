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
                if len(stack) == 0 or stack[-1] + p not in complete:
                    return False
                stack.pop()
        print(stack)
        return len(stack) == 0