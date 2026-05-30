class Solution {
    public int climbStairs(int n) {
        int res = 0;

        if (n == 1 || n ==0) {
            return res + 1;
        }

        res = climbStairs(n-1) + climbStairs(n-2);
        return res;
        
    }
}
