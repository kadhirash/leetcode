class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # if needle len == 0, return 0
        
        # for loop with i 
            # needle substr is in haystack
                # if exists, return index, else return -1
                
                
        if len(needle) < 1:
            return 0
        
        for i in range(len(haystack)):
            if haystack[i: i+ len(needle)] == needle:
                return i
        return -1