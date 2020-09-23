class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # q's:
            # same length
            # True 
        
        # strat:
            # check if exists + same size
            # hashmap to keep track of values in s and t
                # iterate through s 
                    # inc through s and dec. through t
        
        if not s and not t:
            return True
        if len(s) != len(t):
            return False
        
        ans = collections.defaultdict(int)
        
        for letters in range(len(s)):
            ans[s[letters]] += 1
            ans[t[letters]] -= 1
            
        for letters in ans:
            if ans[letters] != 0:
                return False
        return True