class Solution:
    def findMin(self, nums: List[int]) -> int:
        print(nums)
        min_num = min(nums)
        rot = nums.index(min_num)
        

        return min_num

    