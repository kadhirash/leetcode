class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # keep track of len(nums)
        # count num vals 
        # subtract len(nums) - count vals
        
        
        front = 0
        back = len(nums) - 1
        
        while front <= back:
            if nums[front] == val:
                nums[front], nums[back] = nums[back], nums[front]
                back -= 1
            else:
                front += 1
        return front 
        
            