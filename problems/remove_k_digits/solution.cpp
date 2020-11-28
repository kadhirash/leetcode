class Solution {
public:
    string removeKdigits(string num, int k) {
        vector <char> ans; // vector of characters
        if(k == num.size()){
            return "0"; 
        }
        int pos = 0; // position
        while(pos < num.size()){
            int a = ans.size();
            while (k && a && ans[a - 1] > num.at(pos)){
                k --; 
                ans.pop_back(); // remove
                a = ans.size();
            }
            ans.push_back(num.at(pos++));
        }
        while(k --> 0){
            ans.pop_back();
        }
        int a = ans.size();
        string subs = "";
        while(!ans.empty()){
            subs = ans[a-1] + subs;
            a--;
            ans.pop_back();
        }
        while(subs.size() > 1 && subs[0] == '0'){
            subs = subs.substr(1);
        }
        return subs;
    }
};