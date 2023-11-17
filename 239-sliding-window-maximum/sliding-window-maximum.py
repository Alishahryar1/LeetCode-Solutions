class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        q = deque()
        for i in range(k - 1):
            while (q and (nums[q[-1]] < nums[i])):
                q.pop()
            q.append(i)
        
        res = []
        for i in range(k - 1, len(nums)):
            while (q and (nums[q[-1]] < nums[i])):
                q.pop()
            q.append(i)
            res.append(nums[q[0]])
            if q[0] == i - k + 1:
                q.popleft()

        return res