class Solution:
    def romanToInt(self, s: str) -> int:
        dicts = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        result = prev = 0
        
        for i in reversed(s):
            if dicts[i] >= prev:
                result += dicts[i]
            else:
                result -= dicts[i]
            prev = dicts[i]
        return result