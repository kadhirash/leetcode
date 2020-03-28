class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        vector <int> ans (nums.size(), 0);
        for(int i = 0; i < nums.size(); i++){
            int temp = nums[i];
            for(int j = 0; j < nums.size(); j++) {
                if(temp > nums[j]){
                    ans[i]++;
                }
            }
        }
         return ans;
    }
};