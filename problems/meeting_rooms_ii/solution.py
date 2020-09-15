class Solution:
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
            # iterate through the intervals
                # if the prev meetings end time > curr meeting start time
                    # create a new room, push curr meeting end time to heap (now top element)
                # else: pop
            # return len of minheap
            
            
            
            
        import heapq    
        if not intervals: return 0
        intervals.sort(key = lambda x : x[0])
        
        ans = [] 
        
        heapq.heappush(ans, intervals[0][1]) # end time
        
        for meeting_time in intervals[1:]:
            if ans[0] <= meeting_time[0]:
                 heapq.heappop(ans)
            heapq.heappush(ans,meeting_time[1])
        return len(ans)        
        
        