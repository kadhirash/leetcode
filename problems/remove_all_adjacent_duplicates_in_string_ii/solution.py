class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # dummy stack with char, count
            # if count == k: remove
            # else if same char: inc. count
            # else append
            
        # join as a string
        
        
        ans = [['#', 0]]
        
        for char in s:
            if ans[-1][0] == char:
                ans[-1][1] += 1
                if ans[-1][1] == k:
                    ans.pop()
            else:
                ans.append([char,1])
                
                
        string = ''
        for i in range(len(ans)):
            string += ans[i][0] * ans[i][1]
            
        return string
        