class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # clarifications:
            # sorted
            # ints k, x
            # arr[mid] and arr[mid+k] >  x; then x-arr[mid] is neg. and arr[mid+k]-x is pos., 
                # right = mid - 1
            
            # arr[mid] and arr[mid+k] < x; then x-arr[mid] is pos. and arr[mid+k]-x is neg., 
                # left = mid + 1
                
            # arr[mid] < x < arr[mid+k]; since both positive, choose the closer one
        # todo:
            # find k closest elements to x in ascending order
                # if tie, choose the smallest elements
        
        # strategy:
            # use binary search since sorted 
                # O(logn)
        
    
        left, right = 0, len(arr) - k
        while left < right:
            mid = left + (right-left) // 2  
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1 # 1 -> 2 
            else:
                right = mid
        return arr[left:left + k] # return from left --> left + k 