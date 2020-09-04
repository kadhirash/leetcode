class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        intervals.sort(key=lambda x:x[0]) # Sort by start times for intervals
        heap = [intervals[0][1]]
        for meeting in intervals[1:]:
            # check if earliest meeting ends in room will finish before curr. meeting
            # remove earliest meeting
            if heap[0] <= meeting[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, meeting[1])
            # add curr meeting
        return len(heap)