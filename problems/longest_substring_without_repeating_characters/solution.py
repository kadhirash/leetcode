class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # q/a:
            # abcdec
        # return None if no s
        
        # eg:   v  
            # abcabcabc
              #A 
        # strat:
            # anchor 
            
        # edge case 
        if not s:
            return 0
        # init
        
        ans = {}
        anchor = max_len = 0
        
        for char in range(len(s)):
            if s[char] in ans and ans[s[char]] >= anchor:
                anchor = ans[s[char]] + 1
            else:
                max_len = max(max_len, char - anchor + 1)
            ans[s[char]] = char
            
        return max_len