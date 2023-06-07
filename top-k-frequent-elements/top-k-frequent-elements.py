class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = {}
        for num in nums:
            counts[num] = 0
        for num in nums:
            counts[num] += 1
        
        L = []
        for i in range(k):
            max_count = 0
            m = 0
            for num, count in counts.items():
                if count > max_count:
                    m = num
                    max_count = count
            L.append(m)
            counts[m] = 0
        return L
    