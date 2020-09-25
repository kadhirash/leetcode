class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # ex:
           # abcdef" -> 6
        # strat:
            # hashmap
            # anchor start at the beg. 
            # max_len 
            
            
        visited = {}
        
        max_len = anchor = 0
        
        for char in range(len(s)):
            if s[char] in visited and visited[s[char]] >= anchor:
                anchor = visited[s[char]] + 1
                
            else:
                max_len = max(max_len, char-anchor + 1)
            
            visited[s[char]] = char
        return max_len
                
            