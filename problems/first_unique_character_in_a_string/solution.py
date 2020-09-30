class Solution:
    def firstUniqChar(self, s: str) -> int:
        ans = defaultdict(int)
        
        for c in s:
            if c in ans:
                ans[c] += 1
            else:
                ans[c] = 1
        
        
        
        
        for c in ans:
            if ans[c] == 1:
                return s.index(c)
        return -1