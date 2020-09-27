import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # sort 
            # start times
        # min heap
            # end times 
        # [30]  comp. [5] 
        # [10,30]
        # [10] comp. [15]
            #pop 
        # [20,30]
            # return len heap
            
        # edge case    
        if not intervals: return 0
        
        intervals.sort(key = lambda x : x[0])
        
        heap = []
        
        heapq.heappush(heap,intervals[0][1]) # [30]
        
        
        for i in range(1,len(intervals)):
            if heap[0] <= intervals[i][0]:
                heapq.heappop(heap)
            heapq.heappush(heap,intervals[i][1])
            
        return len(heap)