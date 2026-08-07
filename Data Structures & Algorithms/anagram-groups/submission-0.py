class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []


        mp= {}
        for i, s in enumerate(strs):
            freq_arr = [0] * 26

            for c in s:
                freq_arr[ord(c) - ord('a')] += 1
            
            tp_freq = tuple(freq_arr)
            if tp_freq not in mp:
                mp[tp_freq] = [s]
            else:
                mp[tp_freq].append(s)
        
        
        return list(mp.values())