class TrieNode:
    def __init__(self):
        self.childern = {}
        self.isWord = False


class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        newRoot = self.root
        for ch in word:
            if ch not in newRoot.childern:
                newRoot.childern[ch] = TrieNode()
            newRoot = newRoot.childern[ch]
        newRoot.isWord = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """

        def searchSubString(node, index):
            if index == len(word):
                return node.isWord
            ch = word[index]
            if ch == '.':
                for child in node.childern.values():
                    if searchSubString(child, index + 1):
                        return True
            if ch in node.childern:
                return searchSubString(node.childern[ch], index + 1)

            return False

        return searchSubString(self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)