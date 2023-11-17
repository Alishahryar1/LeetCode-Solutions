class Solution(object):
    def fixDeque(self, q, i, nums):
        while (q and (nums[q[-1]] < nums[i])):
            q.pop()
    
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        q = deque()
        for i in range(k - 1):
            self.fixDeque(q, i, nums)
            q.append(i)
        
        res = []
        for i in range(k - 1, len(nums)):
            self.fixDeque(q, i, nums)
            q.append(i)
            res.append(nums[q[0]])
            if q[0] == i - k + 1:
                q.popleft()

        return res