class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        str, pattern = str.split(), list(pattern)
        return list(map(str.index, str)) == list(map(pattern.index, pattern))