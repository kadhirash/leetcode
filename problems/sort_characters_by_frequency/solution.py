class Solution:
    import heapq, collections
    def frequencySort(self, s: str) -> str:
        # sort by decreasing freq. based on chars.
        count = collections.Counter(s)
        k = len(count)
        ans = ''
        for ch in heapq.nsmallest(len(count), count, key = lambda ch: (-count[ch], ch)):
            ans += ch * count[ch]
        return ans
