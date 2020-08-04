class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # 1 Binary search
        # TC: O(log(nm))
        # SC: O(1)
#         if not matrix or len(matrix) == 0:
#             return False
#         row, col = len(matrix), len(matrix[0])
        
#         left,right = 0, row*col-1
        
#         while left <= right:
#             mid = left + (right-left) // 2
#             mid_elem = matrix[mid // col][mid % col]
            
#             if mid_elem == target:
#                 return True
#             elif mid_elem > target:
#                 right = mid - 1
#             else:
#                 left = mid + 1
#         return False
        
        # 2 Binary searches
        # TC: O(max(log n, log m))
        # SC: O(1)
        
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        '''
        Use binary search to find the right row and target
        '''
        top_row, bot_row, row = 0, len(matrix) - 1, -1 # set row to -1 to represent not in matrix
        while top_row <= bot_row:
            mid = top_row + (bot_row-top_row) // 2
            if matrix[mid][0] > target: # target on a higher row
                bot_row = mid - 1
            elif matrix[mid][row] < target: # target on a lower row
                top_row = mid + 1
            else:
                row = mid #target is in this row, and row will now have value of mid
                break
        if row == -1: # no target found
            return False

        """
        Binary search to find target 
        """
        left_col, right_col = 0, len(matrix[0]) - 1
        
        while left_col <= right_col:
            mid = left_col + (right_col-left_col) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target: #target on left side
                right_col = mid - 1
            else: #target on right side
                left_col = mid + 1


        # Different approach 2 binary
#         if len(matrix) == 0:
#             return False
#         # search to find correct row
#         top, bottom = 0, len(matrix) - 1
#         while top < bottom:
#             middle = (top + bottom) // 2 + 1
#             if matrix[middle][0] == target: return True
#             elif matrix[middle][0] < target:
#                 top = middle
#             else:
#                 bottom = middle - 1
                
#         # search the target for this specific row
#         left, right = 0, len(matrix[0]) - 1
#         while left <= right:
#             middle = (left + right) // 2
#             if matrix[top][middle] == target: return True
#             elif matrix[top][middle] < target:
#                 left = middle + 1
#             else:
#                 right = middle - 1
#         return False
        
        
        
        
        