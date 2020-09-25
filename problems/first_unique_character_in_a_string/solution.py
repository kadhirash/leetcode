class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        ans = {}
        
        for letters in range(len(s)):
            if s[letters] not in ans:
                ans[s[letters]] = 1
            else:
                ans[s[letters]] += 1
                
        
        
        for letters in ans:
            if ans[letters] == 1:
                return s.index(letters)
        return -1