class Solution {
public:
    int findNumbers(vector<int>& nums) {
        int evenCount = 0;
        for(int i:nums){
            int digits = 0;
            while(i){
                i /= 10;
                digits++;   
            }
                evenCount += (digits % 2 == 0);
        }
        
        return evenCount;
    }
};