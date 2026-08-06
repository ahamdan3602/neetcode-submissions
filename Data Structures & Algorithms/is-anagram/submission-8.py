class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        my_dict = {}


        for c in s:
            if c not in my_dict:
                my_dict[c] = 1
            else:
                my_dict[c] += 1

        print(my_dict)
        for c in t:
            if c in my_dict:
                my_dict[c] -= 1
        
        print(my_dict)

        for num in my_dict.values():
            if num != 0:
                return False
        return True
        # freq_arr = [0] * 26


        # for i, c in enumerate(s):
        #     freq_arr[ord(s[i]) - ord('a')] += 1
        #     freq_arr[ord(t[i]) - ord('a')] -= 1
        
        # for num in freq_arr:
        #     if num != 0:
        #         return False
        # return True    