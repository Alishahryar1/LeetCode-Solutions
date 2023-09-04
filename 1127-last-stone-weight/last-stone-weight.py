class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        for i, stone in enumerate(stones):
            stones[i] = -stone
        heapq.heapify(stones)
        
        while (len(stones) > 1):
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)
            heapq.heappush(stones, x - y)

        return -heapq.heappop(stones)