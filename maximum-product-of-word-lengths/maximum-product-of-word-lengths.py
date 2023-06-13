class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        letters_present = {}
        for word in words:
            letters_present[word] = [False] * 26
            for letter in word:
                letters_present[word][ord(letter) - 97] = True
        
        product_max = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                product = len(words[i]) * len(words[j])
                if product > product_max:
                    for k in range(26):
                        if letters_present[words[i]][k] and letters_present[words[j]][k]:
                            break
                    else:
                        product_max = product
        
        return product_max