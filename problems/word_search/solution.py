class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        row_len, col_len = len(board), len(board[0])
        
        for row in range(row_len):
            for col in range(col_len):
                if self.dfs(row,col,board,word,0):
                    return True
        return False
    
    
    
    def dfs(self,row,col,board,word,char):
        # validation check
        row_len, col_len = len(board), len(board[0])
        if char == len(word):
            return True
        
        if row < 0 or col < 0 or row >= row_len or col >= col_len or board[row][col] != word[char]: return False
        
        
        # save the board state
        
        state = board[row][col]
        
        
        # mark visited
        
        board[row][col] = '#'
        
        # up,down,left,right
        ans =   self.dfs(row-1,col,board,word,char + 1) or \
                self.dfs(row+1,col,board,word,char + 1) or \
                self.dfs(row,col+1,board,word,char + 1) or  \
                self.dfs(row,col-1,board,word,char + 1)
        
        # reset board state
        
        board[row][col] = state
        
        return ans