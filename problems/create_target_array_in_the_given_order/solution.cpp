class Solution {
public:
    vector<int> createTargetArray(vector<int>& nums, vector<int>& index) {
        vector <int> targetArr;
        for(int i = 0; i < nums.size(); i++){
            targetArr.insert(targetArr.begin() + index[i], nums[i]);
        }
        return targetArr;
    }
};