from _heapq import heappush
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        mp = Counter()

        for i, num in enumerate(nums):
            mp[num] += 1
        
        res = []
        while k > 0:
            grt_val = 0
            kth_grt_elem = 0
            for key in mp:
                if mp[key] > grt_val:
                    kth_grt_elem = key
                    grt_val = mp[key]
            res.append(kth_grt_elem)
            mp.pop(kth_grt_elem)
            k -= 1
        
        return res
            