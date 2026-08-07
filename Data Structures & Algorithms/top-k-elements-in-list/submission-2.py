class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}


        for i in range(len(nums)):
            if nums[i] not in mp:
                mp[nums[i]] = 1
            else: 
                mp[nums[i]] += 1
        

        res = []
        while k > 0:
            greatest_val = 0
            kth_greatest_elem = 0 
            for key in mp:
                if mp[key] > greatest_val:
                    kth_greatest_elem = key
                    greatest_val = mp[key]

            res.append(kth_greatest_elem)
            mp.pop(kth_greatest_elem)
            k -= 1


        return res