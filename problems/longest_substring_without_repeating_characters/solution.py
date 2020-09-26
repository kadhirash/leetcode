class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # ex:
            # abc abc bb
        # hashmap -> visited
        # pointers/sliding window
            # anchor, max_len
            
        # edge case
        if not s:
            return 0
        
        # init
        visited = {}
        anchor = max_len = 0
        
        for char in range(len(s)):
            if s[char] in visited and visited[s[char]] >= anchor:
                # update anchor
                anchor = visited[s[char]] + 1
            else:
                # update max_len
                max_len = max(max_len, char-anchor+1)
            visited[s[char]] = char
        
        return max_len
            