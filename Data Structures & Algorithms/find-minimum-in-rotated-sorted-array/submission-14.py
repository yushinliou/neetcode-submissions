class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        minNum = nums[0]
        while(l <= r):
            if nums[l] < nums[r]:
                minNum = min(minNum, nums[l])
                break
            mid = (r + l) // 2
            if nums[mid] < minNum:
                minNum = nums[mid]
            # if the left side is sorted
            if nums[l] <= nums[mid]:
                l = mid + 1 # check right side
            # check left side
            else:
                r = mid - 1
        return minNum
