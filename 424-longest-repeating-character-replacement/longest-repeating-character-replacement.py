class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        L = R = 0
        counts = [0] * 26
        maxlen = 0
        while (R < len(s)):
            index = ord(s[R]) - ord('A')
            counts[index] += 1
            length = R - L + 1
            replace = length - max(counts)
            if replace <= k:
                maxlen = max(maxlen, length)
            else:
                while replace > k:
                    index = ord(s[L]) - ord('A')
                    counts[index] -= 1
                    L += 1
                    length = R - L + 1
                    replace = length - max(counts)
            
            R += 1
        return maxlen