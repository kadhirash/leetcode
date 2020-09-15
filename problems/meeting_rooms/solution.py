class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Clarifications:
            # not sorted 
        # To Do:
            # Check if a person can make all meetings
        # Example:
            # [[0,30],[5,10],[15,20]] -> [si,ei]
            # False
            
            # [[7,10],[2,4]]
            # True
        # Strategy:
            # Sort by the start times 
            # iterate through the intervals
                # Check if curr meeting start time < prev meeting end time
                    # return False
                # return True
                
        
        if not intervals: return True
        intervals.sort(key = lambda x: x[0])
        
        for meeting_time in range(1,len(intervals)):
            if intervals[meeting_time][0] < intervals[meeting_time-1][1]:
                return False
        return True
        
            
            
            