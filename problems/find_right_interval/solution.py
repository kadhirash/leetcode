class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # ans = [None] * len(intervals)
        # for i in range(len(intervals)):
        #     minimum, minimum_index = float('inf'), -1
        #     for j in range(len(intervals)):
        #         if intervals[j][0] >= intervals[i][1] and intervals[j][0] < minimum:
        #             minimum = intervals[j][0]
        #             minimum_index = j
        #     ans[i] = minimum_index
        # return ans     
        
        sorted = []
        for i in range(len(intervals)):
            sorted.append([intervals[i], i])
        sorted.sort()
    
        result = [-1]*len(intervals)
        
        def binary_search(x):
            if sorted[len(intervals)-1][0][0] < x: return -1
            l,r = 0, len(intervals) - 1
            while l <= r:
                mid = l + (r-l) // 2
                if sorted[mid][0][0] >= x:
                    r = mid - 1
                else:
                    l = mid + 1
            return sorted[l][1]
        for i in range(len(intervals)):
            result[i] = binary_search(intervals[i][1])
        return result