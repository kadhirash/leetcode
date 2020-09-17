class Solution:
    def firstUniqChar(self, s: str) -> int:
        ans = {}
        for char in s:
            if char not in ans:
                ans[char] = 0
            else:
                ans[char] = 1
                
                
        for i in ans:
            if ans[i] == 0:
                return s.index(i)
        return -1