class Solution(object):
    def helper(self, curr, stack, output, n, l_count, r_count):
        if l_count == n and r_count == n:
            output.append(curr)
            return
        if l_count < n:
            self.helper(curr + '(', stack + [')'], output, n, l_count + 1, r_count)
        if r_count < n and len(stack) > 0:
            self.helper(curr + stack[-1], stack[:-1], output, n, l_count, r_count + 1)

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        output = []
        stack = []
        self.helper("", stack, output, n, 0, 0)
        return output