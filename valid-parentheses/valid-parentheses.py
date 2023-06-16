class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for p in s:
            if p in ['(', '{', '[']:
                stack.insert(0, p)
            else:
                if len(stack) == 0:
                    return False
                if p == ')' and stack[0] != '(' or p == ']' and stack[0] != '[' or p == '}' and stack[0] != '{':
                    return False
                del stack[0]
        if len(stack) > 0:
            return False
        return True