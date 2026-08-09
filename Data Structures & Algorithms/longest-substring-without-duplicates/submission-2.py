from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        cur_len = 0
        char_set = set()

        if len(s) == 1:
            return 1


        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_len = max(len(char_set), max_len)
            


        return max_len
            
        