class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>(); // val : idx

        int i = 0;
        for (int n : nums) {
            int diff = target - n;
            if (map.containsKey(diff)) {
                int[] idx = {map.get(diff), i};
                return idx;
            }
            map.put(n, i);
            i++;
        }

        return null;
    }
}
