import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # given start and end times, find min. number of conference rooms
        
        # [[0,30], [15,20]], [5,10]
        
        # sort by interval start time
        # [[0,30], [5,10], [15,20]]
        
        # use minheap
            # push in values of the prev. end time and compare with curr start time
            # if prev end time > curr start time, push in curr_end time, else pop off 
                # [0,30] --> 30
                # since 30 > 5, i can push in 10
                
                # [10,30]
                    # 10 < 15 !
                # [20, 30]
                # return len of heap = # of rooms
                
                
        if not intervals: return 0
        
        
        intervals.sort(key=lambda x:x[0])
        
        rooms = [] # minheap
        
        heapq.heappush(rooms,intervals[0][1])
        
        for i in range(1,len(intervals)):
            if rooms[0] <= intervals[i][0]:
                heapq.heappop(rooms)

            heapq.heappush(rooms,intervals[i][1])
        return len(rooms)
            
        
        
                
                
                
                