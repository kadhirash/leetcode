class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        class TrieNode:
            def __init__(self):
                self.children = defaultdict(TrieNode)
                self.words = []
            def insert(self, word):
                if len(self.words) < 3:
                    self.words.append(word)
                    
                    
        products = sorted(products)
        root = TrieNode()
        
        for i in products:
            curr = root
            for c in i:
                curr = curr.children[c]
                curr.insert(i)
                
        res,curr = [], root
        for c in searchWord:
            curr = curr.children[c]
            res.append(curr.words)
        return res
        