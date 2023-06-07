class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = {}
        hashcodes = []
        for string in strs:
            hashcode = [0] * 26
            for letter in string:
               hashcode[ord(letter) - 97] += 1
            hashcode = tuple(hashcode)
            hashcodes.append(hashcode)
            hashmap[hashcode] = []
        
        for i, string in enumerate(strs):
            hashmap[hashcodes[i]].append(string)

        return hashmap.values()
