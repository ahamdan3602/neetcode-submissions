from _heapq import heappush
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = Counter()


        for num in nums:
            mp[num] += 1
        
        res = []
        
        while k > 0:
            kth_greatest_elem = 0
            kth_curr_elem = 0

            for key in mp:
                if mp[key] > kth_curr_elem:
                    kth_greatest_elem = key
                    kth_curr_elem = mp[key]
            res.append(kth_greatest_elem)
            mp.pop(kth_greatest_elem)
            k -= 1
        
        return res

            