class Solution:
    import heapq, collections
    def frequencySort(self, s: str) -> str:
        # Count the number of occurrences of each unique character in the input string
        counts = {}
        for c in s:
            counts[c] = counts.get(c, 0) + 1
            
        # Descending sort by number of occurrence (frequency), but ascending sort by character (lexicographic)
        
        sortedCounts = sorted((-n, c) for c, n in counts.items())
                
        # Concatenate character sequences
        
        ans = []
        for n, c in sortedCounts:
            ans.append(c*-n)
        return ''.join(ans)


