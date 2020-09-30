class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ans = defaultdict(int)
        
        if len(s) != len(t):
            return False
        for c in range(len(s)):
            ans[s[c]] += 1
            ans[t[c]] -= 1
        
        
        for c in ans:
            if ans[c] != 0 :
                return False
        return True