class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for row in range(len(board)):
            for col in range(len(board[0])):
                if self.dfs(board,row,col,word,0):
                    return True
        return False
    
    def dfs(self,board,row,col,word,i):
        if i == len(word): return True
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or board[row][col] != word[i]: return False
        
        state = board[row][col]
        
        board[row][col] = ''
        
        ans = self.dfs(board,row+1,col,word,i+1) or self.dfs(board,row-1,col,word,i+1) or self.dfs(board,row,col+1,word,i+1) or self.dfs(board,row,col-1,word,i+1)
        
        board[row][col] = state
        
        return ans