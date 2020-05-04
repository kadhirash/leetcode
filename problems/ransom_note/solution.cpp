class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
       vector<int>ans(26,0);
        for(int i=0;i<magazine.size();i++){
         ans[magazine[i]-'a']++;   
        }
        for(int i=0;i<ransomNote.size();i++){
         if(ans[ransomNote[i]-'a']-- <=0 ){
              return 0;
          }   
        }
      return 1;
    }
};