class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        curr_water = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                curr_water = 0
                curr_water = min(heights[i], heights[j]) * abs(j-i)
                if curr_water > max_water:
                    max_water = curr_water
        return max_water