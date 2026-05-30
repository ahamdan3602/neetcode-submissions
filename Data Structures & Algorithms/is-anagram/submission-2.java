class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> map = new HashMap<>();

        HashMap<Character, Integer> map2 = new HashMap<>();


        for (char c : s.toCharArray()) {
            if (!map.containsKey(c)) {
                map.put(c, 1);
            } else {
                map.put(c, map.get(c) + 1);
            }
        }
          for (char c : t.toCharArray()) {
            if (!map2.containsKey(c)) {
                map2.put(c, 1);
            } else {
                map2.put(c, map2.get(c) + 1);
            }
        }
        System.out.println(map);
        System.out.println(map2);


        return map.equals(map2);
       
    }
}
