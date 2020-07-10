class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    
        substring = set()
        left = right = 0
        length = 0
        
        while left < (len(s)) and right < (len(s)):
            if s[right] not in substring:
                substring.add(s[right])
                right += 1
                length = max(length, right - left)
            else:
                substring.remove(s[left])
                left +=1 
        return length