class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_arr = 26 * [0]


        for c in s:
            freq_arr[ord(c) - ord('a')] += 1
        
        for c in t:
            freq_arr[ord(c) - ord('a')] -= 1

        if all(x == 0 for x in freq_arr):
            return True

        return False
        