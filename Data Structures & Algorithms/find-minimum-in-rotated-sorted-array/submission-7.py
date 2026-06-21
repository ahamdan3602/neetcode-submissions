class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        Rotating array n times shifhe array shifts it back to it's original position
        '''
        nums.sort()
        return nums[0]


        