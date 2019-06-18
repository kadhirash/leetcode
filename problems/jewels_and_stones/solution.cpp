class Solution {
public:
    int numJewelsInStones(string J, string S) {
        //J = stones as jewels
            //Distinct, case sensitive letters
        //S = stones
            //Each char. in s = stone
        // How many S are J?
        int count = 0;
        for( int i = 0; i < S.length(); i ++){
            for(int j = 0; j < J.length(); j++){
                 if(J.at(j) == S.at(i)){
                    count++;
                }
            }
        }
        return count;
    }
};