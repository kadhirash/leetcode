import collections
from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # same length, only lowercase alphabets
        # consist of the same amount of characters
        
        # 3 t's, 4 d's, 5 c's 
        # s= tttddddccccc.     t= tcdtcdtcddcc
        
        # use hashmap to keep track of values and indexes
        # iterate through string s 
            # increment s values, decrement t values and compare
        
        # iterate through hashmap
            # if letters in hashmap !0, return False else true
        
        if len(s) != len(t): return False
        
        anagram = defaultdict(int)
        
        for letters in range(len(s)):
            anagram[s[letters]] += 1
            anagram[t[letters]] -= 1
            
        for letters in anagram:
            if anagram[letters] != 0:
                return False
        return True