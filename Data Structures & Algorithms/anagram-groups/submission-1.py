class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}


        for i, wrd in enumerate(strs):
            freq_arr = 26 * [0]
            for c in wrd:
                freq_arr[ord(c) - ord('a')] += 1
            if tuple(freq_arr) not in mp:
                mp[tuple(freq_arr)] = [wrd]
            else:
                mp[tuple(freq_arr)].append(wrd)
        
        return list(mp.values())