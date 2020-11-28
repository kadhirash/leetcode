class Leaderboard:

    def __init__(self):
        self.dict = collections.defaultdict(int)
    
    def addScore(self, playerId: int, score: int) -> None:
        self.dict[playerId] += score

    def top(self, K: int) -> int:
        heap = []
        for x in self.dict.values():
            heappush(heap, x)
            if len(heap) > K:
                heappop(heap)
        res = 0
        while heap:
            res += heappop(heap)
        return res

    def reset(self, playerId: int) -> None:
        del self.dict[playerId]


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)