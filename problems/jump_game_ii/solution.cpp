class Solution {
public:
    int jump(vector<int>& nums) {
        if(nums.empty() || nums.size() == 1) {
        return 0;
      }

      int n = nums.size();
      int jumps = 0;
      int maxLoc = 0; //performs the same logic where you greedily take the maximum jump value
      int curLoc = 0; //

      for(int i = 0; i < n-1; i++) {
        maxLoc = max(maxLoc, i+nums[i]);
        /*
        2:0
        3:1
        1:1
        1:1

        max(0, 0+2) == 2
        max(2, 1+3) == 4
        max(4, 1+1) == 4
        */
        if(curLoc == i) {
          curLoc = maxLoc;
          jumps++;
        }
      }
      return jumps;
    }
};