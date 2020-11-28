class Solution {
public:
    string toLowerCase(string str) {
        for(int i = 0; i < str.length(); i++)
        {
            if (str.at(i) >= 'A' && str.at(i) <= 'Z')
            {
                str.at(i) = str.at(i) - 'A' + 'a';
            }
        }
        return str;
    }
};