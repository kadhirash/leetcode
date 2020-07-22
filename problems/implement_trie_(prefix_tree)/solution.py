class TrieNode:
    def __init__(self):
        self.word = False 
        self.child = {}
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        
        # 1. Initialize: cur = root
        # 2. for each char c in target string S:
        # 3.      if cur does not have a child c:
        # 4.          cur.children[c] = new Trie node
        # 5.      cur = cur.children[c]
        # 6. cur is the node which represents the string S
        
        cur = self.root
        for c in word:
            if c not in cur.child:
               cur.child[c] = TrieNode()
            cur = cur.child[c]
        cur.word = True
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        # 1. Initialize: cur = root
        # 2. for each char c in target string S:
        # 3.      if cur does not have a child c:
        # 4.          search fails
        # 5.      cur = cur.children[c]
        # 6. search successes
        
        cur = self.root
        for c in word:
            if c not in cur.child:
                return False
            cur = cur.child[c]
        return cur.word
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.root
        for c in prefix:
            if c not in cur.child:
                return False
            cur = cur.child[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)