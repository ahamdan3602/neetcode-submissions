class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxArea = 0 

        for i in range(len(heights)):
            for j in range(i, len(heights)):
                width = j - i
                height = min(heights[i], heights[j])

                maxArea = max(maxArea, width * height)

        return maxArea
        