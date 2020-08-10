class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        encountered = {}
        anchor = length = 0
        # for i, e in enumerate(s):
        #     if e in encountered and encountered[e] >= anchor:
        #         anchor = encountered[e] + 1
        #     else:
        #         length = max(length, i-anchor + 1)
        #     encountered[e] = i
        # return length
        for i in range(len(s)):
            if s[i] in encountered and encountered[s[i]] >= anchor:
                anchor = encountered[s[i]] + 1
            else:
                length = max(length, i-anchor + 1)
            encountered[s[i]] = i
        return length