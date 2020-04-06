class Solution {
public:
    int balancedStringSplit(string s) {
        int balance = 0, ans = 0;
        for(int i = 0; i < s.length(); i++){
            if(s.at(i) == 'L'){
                balance++;
            }else if (s.at(i) != 'L'){
                balance--;
            }
            if (balance == 0){
                ans++;
            }
        }
        return ans;
    }
};