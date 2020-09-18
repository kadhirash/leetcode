class Solution:
    import heapq
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # Clarifications:
            # not sorted
        # To Do:
            # find min. # of conference rooms required
        # Example:
            # [0, 30],[5, 10],[15, 20]]
            # 2
        # Strategy:
            # use a min heap -> "min" # of rooms
            # sort by the start times
            # iterate through the intervals starting at 1
                # if the curr heap start_time <= index[0]
                    # create a new room, push curr meeting end time to heap (now top element)
                # else: pop
            # return len of minheap
            
        if not intervals: return 0
        
        rooms = [] # minheap
        
        intervals.sort(key = lambda x:x[0]) # sort rooms by start time
        
        
        heapq.heappush(rooms, intervals[0][1]) # [ [[0, 30],[5, 10],[15, 20]] ]
        
        for meeting_times in range(1,len(intervals)):
            if rooms[0] <= intervals[meeting_times][0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms,intervals[meeting_times][1])
        return len(rooms)
        
        
            
            
        