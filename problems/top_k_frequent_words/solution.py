class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = collections.Counter(words)
        
        heap = []
        
        for word, freq in count.items():
            heap.append((-freq,word))
        
        heapq.heapify(heap)
        
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans