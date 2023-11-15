class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        maxArea = 0
        for i in range(len(heights)):
            j = i
            while (stack and stack[-1][1] > heights[i]):
                 j, h = stack.pop()
                 maxArea = max(maxArea, (i - j) * h)
            stack.append((j, heights[i]))
        
        while stack:
            i, h = stack.pop()
            maxArea = max(maxArea, (len(heights) - i) * h)

        return maxArea
