class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            if token not in ['+','-','/','*']:
                stack.insert(0, int(token))
            else:
                b = stack[0]
                a = stack[1]
                del stack[0]
                del stack[0]
                if token == '+':
                    stack.insert(0, a + b)
                elif token == '-':
                    stack.insert(0, a - b)
                elif token == '/':
                    stack.insert(0, int(float(a)/b))
                else:
                    stack.insert(0, a * b)
        
        return stack[0]