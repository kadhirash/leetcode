import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # hashmap
            # 1 
        
        ans = collections.defaultdict(int)
        
        for char in range(len(s)):
            if s[char] in ans:
                ans[s[char]] += 1
            else:
                ans[s[char]] = 1
        
        for char in ans:
            if ans[char] == 1:
                return s.index(char)
        return -1