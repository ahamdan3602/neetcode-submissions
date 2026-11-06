from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for i, word in enumerate(strs):
            freq_s = [0] * 26
            for c in word:
                freq_s[ord(c) -ord('a')] += 1
            mp[tuple(freq_s)].append(word)

        return list(mp.values())