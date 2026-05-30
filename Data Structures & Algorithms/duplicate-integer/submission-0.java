
class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int num : nums) {
            if (!map.containsKey(num)) {
                map.put(num, 1);
            } else {
                map.replace(num, map.get(num) + 1);
            }
        }
        Collection<Integer> values = map.values();
        ArrayList<Integer> arr = new ArrayList<>(values);
        for (int i = 0; i < arr.size();i++) {
            if (arr.get(i) > 1) {
                return true;
            }
        }

        return false;
 
    }
}
