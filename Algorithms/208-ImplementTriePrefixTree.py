# 前缀树：字典套字典
# ‘#’用来标定单词的边界
class Trie:
    def __init__(self):
        self.trie = {}
        
    def insert(self, word: str) -> None:
        current = self.trie
        for letter in word:
            if letter not in current.keys():
                current[letter] = {}
            current = current[letter]
        current['#'] = '#'

    def search(self, word: str) -> bool:
        current = self.trie
        for letter in word:
            if letter not in current.keys():
                return False
            current = current[letter]
        if '#' in current.keys():
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        current = self.trie
        for letter in prefix:
            if letter not in current.keys():
                return False
            current = current[letter]   
        return True

