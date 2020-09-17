class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # clarifications:
            # only english lowercase/uppercase
            # can start anywhere
        # todo:
            # if word exists -> return true, else false
        # example:  
            # board =[ ['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E']]
                # ABCCED -> True
                # SEE -> True
                # ABCB -> False
            
        # strat:
            # use a dfs 
                # check the left, right, up, down sections
    

    
        
        len_row, len_col = len(board), len(board[0])
        for row in range(len_row):
            for col in range(len_col):
                if self.dfs(row,col,board,word,0):
                    return True
        return False
    
    
        
    def dfs(self,row,col,board,word,char):
        # validation check
        len_row, len_col = len(board), len(board[0])
        if char == len(word): 
            return True
        
        if row < 0 or col < 0 or row >= len_row or col >= len_col or board[row][col] != word[char]: 
            return False
        
        
        # save the state of the board
        state = board[row][col]
        
         # mark visited 
        board[row][col] = '#'
        
        ans = self.dfs(row+1,col,board,word,char+1) or self.dfs(row-1,col,board,word,char+1) or self.dfs(row,col+1,board,word,char+1) or self.dfs(row,col-1,board,word,char+1)
        
        # reset the state
        board[row][col] = state
        
        return ans
            