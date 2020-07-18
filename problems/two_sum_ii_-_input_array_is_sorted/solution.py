class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        front = 0
        back = len(numbers)-1
        
        while front < back:
            sum_ans = numbers[front] + numbers[back] 
            
            if sum_ans == target:
                return (front+1, back + 1)
            
            if sum_ans < target:
                front += 1
            else:
                back -= 1