import collections
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # group anagram strs together, in any order
        # only lower-case english letters -> 26
        # each freq. of letters in each word repeats only once
        
        # put each word's letter in a hashmap, and check the freq of it repeating.
            # whichever one's repeat, put them together
            
        # e, a, t, n, b
        
        
        # if not strs: return ""
        # anagrams = defaultdict(list)
        # for word in strs:
        #     anagrams[''.join(sorted(word))].append(word)
        # return anagrams.values()
        
        if not strs: return ""
        ans = collections.defaultdict(list) # hashmap to count freq.
        for anagrams in strs:
            count = [0] * 26 # since 26 letters, use count to store how many chars repeat
            for chars in anagrams:
                count[ord(chars) - ord('a')] += 1
            ans[tuple(count)].append(anagrams) # group the common pairs together, use tuple since rest aren't hashable?
        return ans.values() # return their values
        
        
        