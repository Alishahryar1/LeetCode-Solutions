class Solution(object):
    def shortestDistance(self, wordsDict, word1, word2):
        """
        :type wordsDict: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        ptr1 = -1
        ptr2 = -1
        min_dist = len(wordsDict)
        for i, word in enumerate(wordsDict):
            if word == word1:
                ptr1 = i
                if ptr2 >= 0:
                    min_dist = min(min_dist, abs(ptr1 - ptr2))
            elif word == word2:
                ptr2 = i
                if ptr1 >= 0:
                    min_dist = min(min_dist, abs(ptr1 - ptr2))
        return min_dist