class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()


    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True

    def dfs(self, root, word):
        curr = root
        for i, c in enumerate(word):
            if c in curr.children:
                curr = curr.children[c]
            else:
                if c == '.':
                    for child in curr.children.values():
                        if self.dfs(child, word[i + 1:]):
                            return True
                    return False
                else:
                    return False

        return curr.end

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return self.dfs(self.root, word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)