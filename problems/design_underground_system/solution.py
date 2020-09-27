import collections
class UndergroundSystem:
    # 2 hashmaps
        # id -> stationName, time
        # startStation,endStation - > total_time, count
    def __init__(self):
        self.check_in_data = {}
        self.journey_data = collections.defaultdict(lambda: [0,0])
        
    def checkIn(self,id, stationName,t):
        self.check_in_data[id] = [stationName,t]
        
    def checkOut(self,id,stationName,t):
        start_station,start_time = self.check_in_data.pop(id)
        
        self.journey_data[(start_station,stationName)][0] += t-start_time # total_time
        self.journey_data[(start_station,stationName)][1] += 1 # count
        
    def getAverageTime(self,startStation,endStation):
        total_time, total_trips = self.journey_data[(startStation,endStation)]
        
        return total_time/total_trips
    
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)