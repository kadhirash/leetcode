class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        intervals.sort(key = lambda x: x[0])
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged
    
    # 1 2 3 4 5 
    # -------
    #       ---
    # ----------
    
    # [1,4], [4,5]
    
    # merged = [[1,4]]
    
    # merged = [[1]]