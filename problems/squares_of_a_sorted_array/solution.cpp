class Solution {
public:
    vector<int> sortedSquares(vector<int>& A) {
        for(int i = 0; i < A.size(); i ++){ // iterate through vector
            A.at(i)= A.at(i) * A.at(i); // square
        }
        // sort  vector answers
        sort(A.begin(), A.end());
        return A; // return vector
    }
};