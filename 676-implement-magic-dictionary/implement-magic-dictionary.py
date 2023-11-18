class MagicDictionary(object):

    def __init__(self):
        self.strings = []

    def buildDict(self, dictionary):
        """
        :type dictionary: List[str]
        :rtype: None
        """
        self.strings = dictionary

    def edit(self, s1, s2):
        count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
        return count
    
    def search(self, searchWord):
        """
        :type searchWord: str
        :rtype: bool
        """
        for s1 in self.strings:
            if len(s1) == len(searchWord) and self.edit(s1, searchWord) == 1:
                return True
        return False


        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)