class Solution {
public:
    int subtractProductAndSum(int n) {
        int product = 1, sum = 0, difference = 1;
        while (n > 0)
        {
            int digit = n%10;
            n /= 10;
            product *= digit;
            sum += digit;
        }
        //cout << product << endl;
        //cout << sum << endl;
        difference = product - sum;
        return difference;
    }
};