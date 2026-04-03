class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # staring from the two side
        # if move the taller wall it would only reduce the max_amount (wide decrease and the height still limited by lower wall)
        # only move the lower one 
        left = 0
        right = len(heights)-1
        curr_water = 0
        max_water = 0
        # for left in range(len(heights)):
        while(left != right):            
            curr_water = min(heights[left], heights[right]) * (right - left)
            if curr_water > max_water:
                max_water = curr_water
            if heights[left] >= heights[right]:
                right -= 1
            else:
                left += 1
        return max_water

