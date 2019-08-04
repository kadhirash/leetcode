class Solution {
public:
    string defangIPaddr(string address) {
        string defang = "";
        for(int i = 0; i < address.length(); i++){
            if(address.at(i) == '.'){
                defang += '[';
                defang += '.';
                defang += ']';
                continue;
            }
            defang += address.at(i);
        }
        return defang;
    }
};