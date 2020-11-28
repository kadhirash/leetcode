class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # get Largest number in array, and add extraCandies to numbers in arr
        
#         # TC: O(n)
#         # SC: O(n)
#         MAX = max(candies)
#         return[candy + extraCandies >= MAX for candy in candies]
        
    
        max_candies = max(candies)
        results = []
        for i in candies:
            if i + extraCandies >= max_candies:
                results.append(True)
            else:
                results.append(False)
        return results