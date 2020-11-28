class Solution {
public:
    string removeVowels(string S) {
        string ans = "";
        for (int i = 0; i < S.length(); i ++){
            if(S.at(i) != 'a' && S.at(i) != 'e' &&
               S.at(i) != 'i' && S.at(i) != 'o' &&
               S.at(i) != 'u'){
                ans += S.at(i);
            }
        }
        return ans;
    }
};