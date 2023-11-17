class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        queue = deque()
        for i in range(k - 1):
            while (queue and (queue[-1][1] < nums[i])):
                queue.pop()
            queue.append((i, nums[i]))
        res = []
        for i in range(k - 1, len(nums)):
            while (queue and (queue[-1][1] < nums[i])):
                queue.pop()
            queue.append((i, nums[i]))
            res.append(queue[0][1])
            if queue[0][0] == i - k + 1:
                queue.popleft()

            #print(queue)
        return res