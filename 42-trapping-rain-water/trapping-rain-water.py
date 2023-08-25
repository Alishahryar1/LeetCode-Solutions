class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_left = [0] * len(height)
        for i in range(1, len(height)):
            max_left[i] = max(height[i - 1], max_left[i - 1])
        
        max_right = [0] * len(height)
        for i in reversed(range(len(height) - 1)):
            max_right[i] = max(height[i + 1], max_right[i + 1])

        collected = 0
        for i in range(len(height)):
            ceil = min(max_right[i], max_left[i])
            collected +=  max(ceil - height[i], 0)

        return collected