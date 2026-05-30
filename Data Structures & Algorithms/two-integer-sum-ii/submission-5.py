class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            val = numbers[l] + numbers[r]
            if val == target and numbers[l] != numbers[r]:
                return [l+1, r+1]
            elif numbers[r] > numbers[l] and val > target:
                r -= 1
            else:
                l += 1
        
        return [-1, -1]

        