class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for arr in matrix:
            print(arr)
            if self.binarySearch(arr, target):
                return True
        return False

    def binarySearch(self, nums: List[int], target: int) -> bool:
        l = 0 
        r = len(nums) - 1


        while l <= r:
            mid = int(l + (r - l) / 2)

            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                l = mid + 1
            else: 
                r = mid - 1

        return False