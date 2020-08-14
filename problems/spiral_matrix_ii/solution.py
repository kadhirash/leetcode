class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res, count = [[None] * n for _ in range(n)], 1
        
        row_beg, row_end, col_beg, col_end = 0, n-1, 0, n-1
        
        while row_beg <= row_end and col_beg <= col_end:
            
            for i in range(col_beg, col_end + 1):
                res[row_beg][i] = count
                count +=1
            row_beg += 1
            
            for i in range(row_beg, row_end+1):
                res[i][col_end] = count
                count += 1
            col_end -= 1
            
            if row_beg <= row_end:
                for i in range(col_end, col_beg -1, -1):
                    res[row_end][i] = count
                    count += 1
            row_end -= 1
            
            if col_beg <= col_end:
                for i in range(row_end, row_beg -1, -1):
                    res[i][col_beg] = count
                    count += 1
            col_beg += 1
        return res
            