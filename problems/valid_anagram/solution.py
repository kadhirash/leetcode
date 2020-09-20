class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # strat:
            # use a hashmap(defaultdict) to keep track 
        
        
        if not s or not t: return True
        
        if len(s) != len(t):
            return False
        
        
        ans = defaultdict(int)
        
        for char in range(len(s)):
            ans[s[char]] += 1
            ans[t[char]] -= 1
            
        
        for char in ans:
            if ans[char] != 0:
                return False
        return True