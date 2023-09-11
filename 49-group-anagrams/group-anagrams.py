class Solution(object):

    def index(self, letter):
        return ord(letter) - 97

    def sort(self, string):
        counts = [0] * 26
        for letter in string:
            counts[self.index(letter)] += 1
        sorted_string = ""
        for i, count in enumerate(counts):
            sorted_string += chr(i + 97) * count
        return sorted_string
    
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = {}
        hashcodes = []
        for string in strs:
            sorted_string = self.sort(string)
            if sorted_string not in hashmap:
                hashmap[sorted_string] = []
            hashmap[sorted_string].append(string)

        return hashmap.values()