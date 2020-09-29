import collections
class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False # end of every word, could also just be a character
    
class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word): # search for words in a Trie
        node = self.root
        for c in word:
            node = node.children[c] # if c isn't added, automatically initialiized to TrieNode via default dict
        node.isWord = True
    
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        trie = Trie()
        node = trie.root
        for w in words:
            trie.insert(w)
        for row in range(len(board)):
            for col in range(len(board[0])):
                self.dfs(board, node, row, col, "", res)
        return res
    
    
    
    def dfs(self, board, node, row, col, path, res):
        
        if node.isWord: # true 
            res.append(path)
            node.isWord = False # reset to false
        
        # validation check
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
            return 
            
        # save state
        tmp = board[row][col]
        
        # get nodes 
        node = node.children.get(tmp)
        
        if not node:
            return 
        # mark visited
        board[row][col] = "#"
        # classic dfs traversal 
        self.dfs(board, node,row+1, col, path+tmp, res)
        self.dfs(board, node, row-1, col, path+tmp, res)
        self.dfs(board, node, row, col-1, path+tmp, res)
        self.dfs(board, node, row, col+1, path+tmp, res)
        # reset state
        board[row][col] = tmp