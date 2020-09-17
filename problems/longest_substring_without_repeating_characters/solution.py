class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        seen = {}
        if not s: return 0
        
        anchor = max_len = 0
        
        for char in range(len(s)):
            if s[char] in seen and seen[s[char]] >= anchor:
                anchor = seen[s[char]] + 1
            else:
                max_len = max(max_len, char - anchor + 1)
            seen[s[char]] = char
            
        return max_len