class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack = []
        total = 0
        for op in operations:
            if op == '+':
                a = stack.pop()
                b = stack[-1]
                stack.append(a)
                stack.append(a + b)
                total += a + b
            elif op == 'C':
                total -= stack.pop()
            elif op == 'D':
                total += stack[-1] * 2
                stack.append(stack[-1] * 2)
            else:
                total += int(op)
                stack.append(int(op))
        
        return total