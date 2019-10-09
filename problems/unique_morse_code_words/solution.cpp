class Solution {
public:
    int uniqueMorseRepresentations(vector<string>& words) {
        vector <string> morseCodes = {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
        
        unordered_set <string> result; 
        for(auto i : words){
            string ans;
            for(auto j: i){
               ans += morseCodes[j-'a']; 
            }
            result.insert(ans);
        }
       return result.size();         
    }
};