class UndergroundSystem:

    def __init__(self):
        self.check_in_data = {} # (id -> (startStation, t))
        
        self.journey_data = collections.defaultdict(lambda:[0,0]) # (startStation, end Station -> total_time, count) 
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in_data[id] = [stationName,t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station,start_time = self.check_in_data.pop(id)
        self.journey_data[(start_station,stationName)][0] += (t-start_time)
        self.journey_data[(start_station,stationName)] [1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_trips, total_count = self.journey_data[(startStation,endStation)]

        return total_trips / total_count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)