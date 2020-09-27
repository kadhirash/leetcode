import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # use hashmap
        # if char --> inc. + 1
        # set to 1
        
        # check where == 1 in hashmap, return index 
        
        
        ans = collections.defaultdict(int)
        
        for c in s:
            if c in ans:
                ans[c] = 1
            else:
                ans[c] = 0
        
        
        for c in ans:
            if ans[c] == 0:
                return s.index(c)
        return -1