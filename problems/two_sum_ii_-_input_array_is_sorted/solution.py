class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        front,back = 0, len(numbers)-1
        
        while front <= back:
            num = numbers[front] + numbers[back]
            if num == target:
                return (front + 1, back + 1)
            elif num < target:
                front += 1
            else:
                back -= 1
        return [-1,-1]