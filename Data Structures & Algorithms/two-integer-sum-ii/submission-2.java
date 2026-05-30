class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int n = numbers.length;


        int L = 0;
        int R = n - 1;
        int[] res = new int[2];

        while (L < R) {
            if (numbers[L] + numbers[R] > target) {
                R--;
            } else if (numbers[L] + numbers[R] < target) {
                L++;
            } else {
                res[0] = L + 1;
                res[1] = R + 1;
                return res;
            }
        }

        return res;
    }

}

