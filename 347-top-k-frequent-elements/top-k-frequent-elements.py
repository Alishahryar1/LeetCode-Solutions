class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        countMap = {}
        for num in nums:
            if num not in countMap:
                countMap[num] = 0
            countMap[num] += 1
        
        L = []
        for key, value in countMap.items():
            L.append([-value, key])
        heapq.heapify(L)
        output = []
        for _ in range(k):
            output.append(heapq.heappop(L)[1])
        return output