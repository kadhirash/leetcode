import collections
import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
#         For example, your object is something like this in tuple's format (key, value_1, value_2)

# When you put the objects (i.e. tuples) into heap, it will take the first attribute in the object (in this case is key) to compare. If a tie happens, the heap will use the next attribute (i.e. value_1) and so on.


        freq_words = collections.Counter(words)
        
        heap = []
        
        for key , val in freq_words.items():
            heapq.heappush(heap, (-val, key))
            
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[-1])
        
        return res
                
            