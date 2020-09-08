class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        ans = [['',0]]
        for chars in s:
            if ans[-1][0] == chars:
                ans[-1][1] += 1
                if ans[-1][1] == k:
                    ans.pop()
            else:
                ans.append([chars,1])
                
    
        return ''.join(chars*k for chars,k in ans)