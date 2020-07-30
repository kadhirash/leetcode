class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # generate prefix products
        prefix_products = [ ]
        for num in nums:
            if prefix_products:
                prefix_products.append(prefix_products[-1]*num)
            else:
                prefix_products.append(num)
        # print(prefix_products) # 1, 2, 6, 24 -> (1), (2*1) , (3 * 2 * 1), ( 4 * 3 * 2 * 1)
        
        suffix_products = [ ]
        for num in reversed(nums):
            if suffix_products:
                suffix_products.append(suffix_products[-1]*num)
            else:
                suffix_products.append(num)
        suffix_products = list(reversed(suffix_products))
        # print(suffix_products) # 24, 24, 12, 4 -> (1 * 2 * 3 * 4), (2 *3 * 4), (3 * 4), (4)
        
        # result of prefix and suffix
        result = [ ]
        for i in range(len(nums)):
            if i == 0:
                result.append(suffix_products[i+1])
                # print(result) (24)
            elif i == len(nums) - 1:
                result.append(prefix_products[i-1])
                #print(result) # (24, 12, 8 , 6)
            else:
                result.append(prefix_products[i-1] * suffix_products[i+1])
                # print(result) -> 24, 12 
                #               -> 24, 12, 8
        # print(result) # 24, 12, 8, 6
        
        return result