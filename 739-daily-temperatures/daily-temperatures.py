class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        index_stack = []
        i = 0
        j = i + 1
        output = [0] * len(temperatures)
        while i < len(temperatures) - 1:
            if temperatures[j] > temperatures[i]:
                output[i] = j - i
                if len(index_stack) == 0:
                    i = j
                    j += 1
                else:
                    i = index_stack.pop()
            else:
                index_stack.append(i)
                i = j
                j += 1
        
        return output