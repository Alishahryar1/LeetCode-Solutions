class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        alt_curr = 0
        alt_max = 0
        for g in gain:
            alt_curr += g
            alt_max = max(alt_max, alt_curr)
        return alt_max