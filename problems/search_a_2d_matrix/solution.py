class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False
        
        row, col = len(matrix), len(matrix[0])
        left, right = 0, (row * col) - 1
        
        while left <= right:
            mid = left + (right-left) // 2
            mid_arr = matrix[mid // col][mid % col]
            if mid_arr == target: return True
            elif mid_arr < target: left +=1
            else: right -= 1
        return False