class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
    # Naive sol: O(n^2); TC     O(n);S
#         #row <-col->
#         for i in range(len(matrix)):
#             for j in range(i, len(matrix)):
#                 matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
#         #reverse row
#         for i in range(len(matrix)):
#             matrix[i].reverse()



        matrix.reverse()
    
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

