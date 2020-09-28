class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # q/a:
            # return False if no s or t
            # same length
        # strat
            # hashmap 
        
        if len(s) != len(t):
            return False
        
        ans = collections.defaultdict(int) 
        
        for char in range(len(s)):
            ans[s[char]] += 1
            ans[t[char]] -= 1
            
        
        for char in ans:
            if ans[char] !=0:
                return False
        return True
            
        