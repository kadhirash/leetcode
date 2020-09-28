class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        if not words or not k:
            return None
        heap = []
        
        count = collections.Counter(words)
        
        
        for word, freq in count.items():
            heap.append((-freq,word))
        
        heapq.heapify(heap)
        
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans
            