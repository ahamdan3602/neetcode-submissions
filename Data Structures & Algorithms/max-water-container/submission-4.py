class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxArea = 0


        l = 0
        r = len(heights) - 1

        while l < r:
            width = r - l
            height = min(heights[r], heights[l])
            maxArea = max(maxArea, width * height)

            if heights[r] > heights[l]:
                l += 1
            else: 
                r -= 1
        return maxArea