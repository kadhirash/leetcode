class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # clarifications:
            # same length for s and t
            # it is valid if none
            
        # todo:
            # return if t is anagram of s
        
        # strat:
            # check to see if s / t exist
            # check the lengths of s and t
            
            # iterate through s, use a hashmap(defaultdict[int]) to store values
                # delete characs
                # incr. chars in t
            # 
        # complexities:
            # time: O()
            # space: O()
            
            
        if not s or not t: return True
        
        if len(s) != len(t): return False
        
        anag = defaultdict(int) 
        
        for char in range(len(s)):
            anag[s[char]] += 1
            anag[t[char]] -= 1
        
        for values in anag:
            if anag[values] != 0: # 1, -1, so on 
                return False
        return True