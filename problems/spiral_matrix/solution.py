class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # # print top row left to right
        # top = 0
        # left = 0
        # right = n - 1
        # direction = 0 # 0 --> 3
        # for i in range(len(matrix)):
        #     bottom = i - 1
        #     for j in range(len(matrix[i])):
        
        ans = [ ]
        while matrix:

            # top
            ans.extend(matrix.pop(0)) 
            print(f'Top matrix extend : {ans}\n')
            
            #right
            if matrix:
                for i in range(len(matrix)):
                    if matrix[i]:
                        ans.append(matrix[i].pop())
                        print(f'Right matrix append: {ans}')
            #bottom
            if matrix:
                ans.extend(matrix.pop()[::-1])
                print(f'Bottom matrix extend : {ans}')
            
            #left
            if matrix:
                for i in range(len(matrix)-1,-1,-1):
                    if matrix[i]:
                        ans.append(matrix[i].pop(0))
                        print(f'Left matrix append : {ans}')
        return ans 