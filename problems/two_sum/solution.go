func twoSum(nums []int, target int) []int {
    hash_map := make(map[int]int)
    
    for i:= 0; i < len(nums); i++{
        hash_map[nums[i]] = i
    }
    
    for i := 0; i < len(nums); i++{
        complement := target - nums[i]
        if _, found := hash_map[complement]; found{
            if hash_map[complement] != i{
                return [] int{i, hash_map[complement]}
            }
        }
    }
    return nil
}
