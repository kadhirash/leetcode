import collections
from collections import defaultdict
class UndergroundSystem:

    def __init__(self):
        self.check_in_data = collections.defaultdict(list)
        self.travel_data = collections.defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in_data[id] = [stationName,t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, prev_time = self.check_in_data[id]
        route = start_station + stationName
        return self.travel_data[route].append(t-prev_time) 

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        route = startStation + endStation
        return sum(self.travel_data[route])/len(self.travel_data[route])

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)