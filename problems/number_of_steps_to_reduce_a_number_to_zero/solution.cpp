class Solution {
public:
    int numberOfSteps (int num) {
        int counter = 0;
        
        while(num != 0){
            if(num % 2 == 1){
                num -= 1;
                //num /= 2;
                counter ++;
                if(num == 0){
                    break;
                }
            }
            if(num % 2 == 0){
                num /= 2;
                counter ++;
            }
            
        }
        return counter;
    }
};