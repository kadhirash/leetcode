import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        ans = collections.defaultdict(int)
        
        for letter in range(len(s)):
            ans[s[letter]] += 1
            ans[t[letter]] -= 1
            
        
        
        for letter in ans:
            if ans[letter] != 0:
                return False
        return True