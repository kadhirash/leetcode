class Solution {
public:
    int calculateTime(string keyboard, string word) {
        int count = 0, index = 0, times = 0;
        for(int i = 0; i < word.length(); i++){
           for(int j = 0; j < keyboard.length(); j ++){
               if(word.at(i) == keyboard.at(j)){
                   count = abs(index-j);
                   index = j;
                   times += count;
               }
           }
        }
         return times;
    }
};