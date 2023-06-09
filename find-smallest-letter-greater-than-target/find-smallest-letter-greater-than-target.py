class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        i_min = -1
        diff_min = 26
        for i, letter in enumerate(letters):
            diff = ord(letter) - ord(target)
            if diff > 0 and diff < diff_min:
                i_min = i
                diff_min = diff
        
        if i_min == -1:
            return letters[0]
        else:
            return letters[i_min]