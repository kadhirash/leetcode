class Solution:
    def frequencySort(self, s: str) -> str:
        count = collections.Counter(s)
        k = len(count)
        ans = ''
        for c in heapq.nsmallest(k,count, key = lambda c: (-count[c], c)):
            ans += count[c] *c
            
        return ans