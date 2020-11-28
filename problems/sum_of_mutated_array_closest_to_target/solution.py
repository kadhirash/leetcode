class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        # value = target / len(arr)
        
        arr.sort()
        arr_len = len(arr)
        
        for i in range(arr_len):
            value = round(target / arr_len)
            
            if arr[i] >= value:
                return value
            else:
                target -= arr[i]
                arr_len -= 1
        return arr[i]