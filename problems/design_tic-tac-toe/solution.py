class TicTacToe:
    # move valid if placed on empty block
    # once winning condition reache'd, no more moves
    # player succeeds in placing "n" of their marks in horiz/vert/or diag. row
    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self. n = n
        self.bboard = [None, 1, -1] 
            # player = -1 if not valid move, 1 if valid move, else None
        self.rows = [0]*n
        self.cols = [0]*n
        # top_left -> bottom_right
        self.diag1 = 0
        # top_right -> bottom_left
        self.diag2 = 0
        
    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        if player != 1 and player != 2: return None
        
        board = self.bboard[player]
        
        # add rows to board
        self.rows[row] += board
        # if the rows == board * n marks
        if self.rows[row] == board*self.n:
            return player
        
        self.cols[col] += board
        if self.cols[col] == board * self.n:
            return player
    
        if row == col:
            self.diag1 += board
            if self.diag1 == board *self.n:
                return player
        if row + col == self.n-1:
            self.diag2 += board
            if self.diag2 == board*self.n:
                return player
        return 0 # no one wins


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)