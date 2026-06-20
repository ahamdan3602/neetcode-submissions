class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l, r = 0, len(heights) - 1
        
        maxRes = 0
        while l < r:
            h = min(heights[l], heights[r])
            w = r - l
            maxRes = max(maxRes, h*w)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxRes
        