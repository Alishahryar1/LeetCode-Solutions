class WordDistance(object):

    def __init__(self, wordsDict):
        """
        :type wordsDict: List[str]
        """
        self.wordsDict = wordsDict
        

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        ptr1 = -1
        ptr2 = -1
        min_dist = len(self.wordsDict)
        for i, word in enumerate(self.wordsDict):
            if word == word1:
                ptr1 = i
                if ptr2 >= 0:
                    min_dist = min(min_dist, abs(ptr1 - ptr2))
            elif word == word2:
                ptr2 = i
                if ptr1 >= 0:
                    min_dist = min(min_dist, abs(ptr1 - ptr2))
        return min_dist
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)