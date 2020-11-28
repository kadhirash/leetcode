class Solution {
public:
    string defangIPaddr(string address) {
        string ans = "";
        for(int i = 0; i < address.length(); i ++){
            if(address.at(i) == '.'){
                //address.at(i) = '[' + '.' + ']';
                ans += "[";
                ans += ".";
                ans += "]";
                continue;
            }
            ans += address.at(i);
        }
        return ans;
    }
};