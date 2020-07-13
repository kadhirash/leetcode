class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        dict1 = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i+j not in dict1:
                    dict1[i+j] = [matrix[i][j]]
                else:
                    dict1[i+j].append(matrix[i][j])
        ans = [ ]
        for i in dict1.items():
            if i[0] % 2 == 0:
                [ans.append(j) for j in i[1][::-1]]
            else:
                [ans.append(j) for j in i[1]]
        return ans