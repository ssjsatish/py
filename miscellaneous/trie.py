class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isEndOfWord = False
class Trie:
    def __init__(self):
        self.root = self.getNode()
    def getNode(self):
        return TrieNode()
    def _charToIndex(self,ch):
        return ord(ch)-ord('a')
    def insert(self,key):
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]
        pCrawl.isEndOfWord = True
    def search(self,key):
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]
        return pCrawl != None and pCrawl.isEndOfWord
def main():
    keys = ['grammar','gratitude','gratification','gorilla','groot','great','grandfather','goosebumps','groovy']
    output = ['not present in trie', 'present in trie']
    trie = Trie()
    for key in keys:
        trie.insert(key)
    print('{}----------{}'.format('groovy', output[trie.search('groovy')]))
if __name__=='__main__':
    main()