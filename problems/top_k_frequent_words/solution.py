import collections
import heapq
from heapq import heapify, heappush, heappop
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        # count freq. of word and add to heap to store best 'k' candidates
            # worst candidates at top of heap, then pop off 'k' times and reverse
            # so best candidates are there
        count = collections.Counter(words)
        #print(count) # {'i':2, 'love': 2, 'leetcode': 1, 'coding': 1}
        heap = [] 
        for word, freq in count.items():
            heappush(heap,(-freq,word))
        # pop top k 
        
        res = []        
        for i in range(k):
            neg_val, key = heappop(heap)
            res.append(key)
        return res
        