from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = Counter()
        l = res = 0

        for r, c in enumerate(s):
            mp[c] += 1
            while mp[c] > 1:
                mp[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
                
