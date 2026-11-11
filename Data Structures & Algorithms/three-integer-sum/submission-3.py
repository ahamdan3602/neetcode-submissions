class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        '''
        l = 0
        r = l + 1
        while r < len(nums):
            k = r + 1
            while k < len(nums):
                if nums[l] + nums[r] + nums[k] == 0:
                    res.add(tuple(sorted([nums[l], nums[r], nums[k]])))
                k += 1
            if r == len(nums) - 1:
                l += 1
                r = l + 1
            else: 
                r += 1

        return [list(t) for t in res]
        '''
        nums.sort()
        for k in range(len(nums)):
            l = k + 1
            r = len(nums) - 1

            if k > 0 and nums[k] == nums[k - 1]:
                continue

            while l < r:
                cur = nums[l] + nums[r] + nums[k]
                if cur == 0 and l != k and r != k:
                    res.append([nums[k], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif cur < 0:
                    l += 1
                else:
                    r -= 1

        return res


