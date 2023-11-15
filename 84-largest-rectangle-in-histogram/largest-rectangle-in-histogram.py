class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        maxArea = 0
        for i, height in enumerate(heights):
            j = i
            while (stack and stack[-1][1] > height):
                 j, h = stack.pop()
                 maxArea = max(maxArea, (i - j) * h)
            stack.append((j, height))
        
        while (stack):
            i, h = stack.pop()
            maxArea = max(maxArea, (len(heights) - i) * h)

        return maxArea
