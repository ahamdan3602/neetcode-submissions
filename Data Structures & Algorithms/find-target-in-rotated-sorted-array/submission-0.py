class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        [3,4,5,6,1,2]
        target = 1

        '''
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1