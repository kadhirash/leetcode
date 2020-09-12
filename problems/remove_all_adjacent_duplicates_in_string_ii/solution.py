class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # choosing 'k' adjacent and equal letters from 's'
            # removing them so left and right side of deleted strings get conctenated
        # repeatedly make 'k'duplicate removals on 's' until we can't
        
        # return final 's'
        
    # Clarifications:
        # s is all lowercase 
        # 2 - k - 10^4 

    # Examples:
        # 'abcd', 2
            # 'abcd'
        # 'deeedbbcccbdaa', 3
            # 'ddbbbdaa' -> removed eee, ccc
            # 'dddaa' -> removed bbb
            # 'aa' -> removed ddd
    
    # Walkthrough
    # keep track of length of string
    # Iterate through the string, w/ count variable
        # If the curr char same as the one after it, then increase the count else reset to 1 
        # if count == k then remove the last k chars
    # repeat until length of string can't be changedd 
    
        i = 0
        while i < len(s):
            if s[i:i+k] == s[i] * k:
                s = s[:i] + s[i+k:]
                i = 0
            else:
                i += 1
        return s
    
     # i=0
     #    while i<len(s):
     #        if s[i:i+k]==s[i]*k:
     #            s=s[:i]+s[i+k:]
     #            i=0
     #        else:
     #            i+=1
     #    return s

        
    
        
    