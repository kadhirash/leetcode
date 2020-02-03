class Solution {
public:
    int numJewelsInStones(string J, string S) {
        int count = 0;
        for(int i = 0; i < S.length(); i ++){
            for(int j = 0; j < J.length(); j++){
                if(S.at(i) == J.at(j)){
                    count++;
                }
            }
        }
        return count;
    }
};