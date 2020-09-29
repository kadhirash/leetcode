class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        # init
        anchor = max_len = 0
        visited = {}

        for char in range(len(s)):
            if s[char] in visited and visited[s[char]] >= anchor:
                anchor = visited[s[char]] + 1
            else:
                max_len = max(max_len, char - anchor + 1)
            visited[s[char]] = char
        return max_len