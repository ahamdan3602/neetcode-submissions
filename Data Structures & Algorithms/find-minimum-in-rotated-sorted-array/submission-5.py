class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        Rotating array n times shifhe array shifts it back to it's original position
        '''
        l, r = 0, len(nums) - 1


        minRes = 1001
        while l < r:
            mid = (l+r) // 2

            # left sorted
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]
