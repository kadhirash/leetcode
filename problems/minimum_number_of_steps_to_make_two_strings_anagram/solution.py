import collections
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count = collections.Counter(s)
        ans = 0
        for c in t:
            if count[c] > 0:
                count[c] -= 1
            else:
                ans += 1
        return ans