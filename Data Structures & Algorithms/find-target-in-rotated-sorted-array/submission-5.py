class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while(l <= r):
            mid = (l + r) // 2
            # check if mid is the answer
            if target == nums[mid]:
                return mid
            if target == nums[r]:
                return r
            if target == nums[l]:
                return l

            # if left side is sorted
            if (nums[l] < nums[mid]):
                # if target within the range, search in the left side
                if (target >= nums[l]) and (target <= nums[mid]):
                    r = mid - 1
                else:
                    # else search in another side
                    l = mid + 1
            else: # right side is sorted
                # check if target in right side
                if (target >= nums[mid]) and (target <= nums[r]):
                    l = mid + 1 # search in the right side
                else:
                    r = mid -1 # search in the left side
        return -1