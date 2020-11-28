class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return None
        row_beg, row_end, col_beg, col_end = 0, len(matrix)-1, 0, len(matrix[0])-1
        res = []
        
        while row_beg <= row_end and col_beg <= col_end:
            
            for i in range(col_beg,col_end + 1):
                res.append(matrix[row_beg][i])
            row_beg += 1
            
            for i in range(row_beg,row_end + 1):
                res.append(matrix[i][col_end])
            col_end -= 1
            
            if row_beg <= row_end:
                for i in range(col_end, col_beg -1, -1):
                    res.append(matrix[row_end][i])
            row_end -= 1
            
            if col_beg <= col_end:
                for i in range(row_end, row_beg-1, -1):
                    res.append(matrix[i][col_beg])
            col_beg += 1
        return res