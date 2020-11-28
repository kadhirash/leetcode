class Solution:
    def findPermutation(self, s: str) -> List[int]:
        ret = []
        for i in range(len(s)):
            if s[i] == 'I':
                ret.extend(range(i + 1, len(ret), -1))
        ret.extend(range(len(s) + 1, len(ret), -1))
        return ret