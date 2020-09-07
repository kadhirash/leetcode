class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = {}
        anchor = length = 0
        
        for i in range(len(s)):
            if s[i] in seen and seen[s[i]] >= anchor:
                anchor = seen[s[i]] + 1
            else:
                length = max(length, i-anchor + 1)
            seen[s[i]] = i
        return length
        
        # encountered = {}
        # anchor = length = 0
        # for i, e in enumerate(s):
        #     if e in encountered and encountered[e] >= anchor:
        #         anchor = encountered[e] + 1
        #     else:
        #         length = max(length, i-anchor + 1)
        #     encountered[e] = i
        # return length
        