class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        :type height: List[int]
        :rtype: int

        height = the shorter line between the two
        width = r - l
        """
        

        l = 0
        r = len(heights) - 1

        maxArea = 0
        while l < r: 
            h = min(heights[l], heights[r])
            w = r - l
            maxArea = max(maxArea, h * w)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxArea



