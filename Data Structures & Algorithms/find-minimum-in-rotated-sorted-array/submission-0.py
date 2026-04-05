class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        minNums = 1000

        for i in range(len(nums)):
            if nums[i] < minNums:
                minNums = nums[i]
        return minNums

        # sLen = len(nums)
        # minNum = 1000
        # mid = sLen // 2
        # l = 0
        # r = len(nums) - 1
        
        # if nums[0] < nums[-1]:
        #     return nums[0]

        # while(0):
        #     if (nums[l] < nums[mid]) and (nums[mid] < nums[r]):
        #         return nums[l]
        #     elif (nums[l] < nums[mid]) and (nums[mid] > nums[r]):
        #         mid = (r - mid) // 2
        #     elif (nums[l] > nums[mid]) and (nums[mid] < nums[r]):
        #         if  nums[mid]
        #         mid = (mid - l) // 2
        #         if nums[mid] 

            