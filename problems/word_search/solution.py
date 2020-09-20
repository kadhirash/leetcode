class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # strat:
            # dfs (row,col, board,word,char)
            
            # mark visited cells
        
        
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if self.dfs(row,col,board,word,0):
                    return True
        return False
    
    
    
    
    def dfs(self, row, col, board, word, char):
        # validation check:
            
        if char == len(word):
            return True
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or board[row][col] != word[char]: return False
        
        
        # save the state
        state = board[row][col]
        
        # mark the visited 
        
        board[row][col] = '#'
        
        
        ans =   self.dfs(row+1,col,board,word, char + 1) or \
                self.dfs(row-1,col,board,word, char + 1) or \
                self.dfs(row,col-1,board,word, char + 1) or \
                self.dfs(row,col+1,board,word, char + 1)
        
        
        # reset to state
        
        board[row][col] = state
        
        
        return ans