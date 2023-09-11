class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = {}
        hashcodes = []
        for string in strs:
            sorted_string = ''.join(sorted(string))
            if sorted_string not in hashmap:
                hashmap[sorted_string] = []
            hashmap[sorted_string].append(string)

        return hashmap.values()