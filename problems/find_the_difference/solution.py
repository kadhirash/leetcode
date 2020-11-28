class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        
        ans = 0
        
        for i in s:
            ans ^= ord(i)
            
        for j in t:
            ans ^= ord(j)
            
        
        return chr(ans)