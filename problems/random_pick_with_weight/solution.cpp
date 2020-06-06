class Solution {
public:
    vector<int> s;
    Solution(vector<int>& w) {
        for (int index : w){
            if(s.empty())
                s.push_back(index);
            else
                s.push_back(index + s.back());
        }
    }
    
    int pickIndex() {
        int x = s.back();
        int index = rand() % x;
        auto it = upper_bound(s.begin(), s.end(),index);
        return it - s.begin();
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(w);
 * int param_1 = obj->pickIndex();
 */