class Trie:

    def __init__(self):
        self.char = None
        self.children = {}
        self.end = False

    def insert(self, word: str) -> None:
        cursor = self
        i = 0
        while i < len(word):
            if word[i] in cursor.children:
                cursor = cursor.children[word[i]]
                i += 1
            else:
                cursor.children[word[i]] = Trie()
                cursor = cursor.children[word[i]]
                cursor.char = word[i]
                i += 1
            if i == len(word):
                cursor.end = True
        
    def search(self, word: str) -> bool:
        cursor = self
        i = 0
        while i < len(word):
            if word[i] not in cursor.children:
                return False
            cursor = cursor.children[word[i]]
            i += 1
        return cursor.end
        

    def startsWith(self, prefix: str) -> bool:
        cursor = self
        i = 0
        while i < len(prefix):
            if prefix[i] not in cursor.children:
                return False
            cursor = cursor.children[prefix[i]]
            i += 1
        return True
        
#  Each node has adjacencies

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)