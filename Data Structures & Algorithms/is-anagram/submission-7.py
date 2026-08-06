class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq_arr = [0] * 26


        for i, c in enumerate(s):
            freq_arr[ord(s[i]) - ord('a')] += 1
            freq_arr[ord(t[i]) - ord('a')] -= 1
        
        for num in freq_arr:
            if num != 0:
                return False
        return True    