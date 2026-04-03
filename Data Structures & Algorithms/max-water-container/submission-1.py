class Solution:
    def maxArea(self, heights: List[int]) -> int:
        heights_copy = heights.copy()
        max_water = 0

        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                curr_water = 0
                bar = min(heights[i], heights[j])

                
                curr_water = bar * abs(j-i)
                # print(f"bar={bar}, min({heights[i]}, {heights[j]}), i={i}, j={j}, curr_w={curr_water}")
                if curr_water > max_water:
                    max_water = curr_water

        return max_water

