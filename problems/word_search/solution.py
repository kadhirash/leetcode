class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # find if word exists
            # word formed by adjacent horizontal/vertical neighboring cells
            # same cell can't be used more than once
        
        
        # 2 x 2 
        # only lower/upper case letters
        
        if not board: return False
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if self.dfs(board,row,col,word,0):
                    return True
        return False
    
    
    def dfs(self,board,row,col,word,char):
        
        # validation checks
        if char == len(word): return True
        
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or board[row][col] != word[char]: return False
        
        
        # curr state
        
        state = board[row][col]
        
        # mark visited
        board[row][col] = '#'
        
        ans = self.dfs(board,row-1,col,word,char+1) or \
        self.dfs(board,row+1,col,word,char+1)or \
        self.dfs(board,row,col-1,word,char+1)or \
        self.dfs(board,row,col+1,word,char+1)
        
        # revert state
        
        board[row][col] = state
        
        return ans