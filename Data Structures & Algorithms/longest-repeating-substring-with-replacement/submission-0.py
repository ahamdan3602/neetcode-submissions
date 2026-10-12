from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = l = 0
        count = Counter()

        for r, c in enumerate(s):
            count[c] += 1
            window_len = (r - l + 1)  - int(count.most_common(1)[0][1])
            if window_len > k:
                count[s[l]] -= 1
                if count[s[l]] == 0:
                    del count[s[l]]
                l += 1
            res = max(r-l+1, res)
        return res


                
'''
AA -> A, K=0,1
AA -> A, k=0,1
ABA -> BA

'''

