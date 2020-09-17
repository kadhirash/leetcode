class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # todo:
            # true if t is anagram of s
        # strat:
            # if len(s) != len(t) return False
            # keep a hashmap of integer values of the chars in s and t
                # increment s, decrement t
                # if len != 0 return False, else True
        
        if len(s) != len(t): return False
        
        anagram = defaultdict(int)
        
        for char in range(len(s)):
            anagram[s[char]] += 1
            anagram[t[char]] -= 1
            
        for values in anagram:
            if anagram[values] != 0:
                return False
        return True