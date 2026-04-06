class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        minNum = nums[0]
        ct = 0
        while(l <= r):
            print(f"round = {ct}")
            ct += 1
            if ct > 10:
                break
            if nums[l] < nums[r]:
                minNum = min(minNum, nums[l])
                print(f"minNum={minNum}, num[l]={nums[l]}")
                break
            print(f"l={l}, r={r}")
            mid = (r + l) // 2
            print(f"mid={mid}")
            if nums[mid] < minNum:
                minNum = nums[mid]
                print(f"curr min = {minNum}")
            # if the left side is sorted
            if nums[l] <= nums[mid]:
                print(f"{nums[l]} <= {nums[mid]}")
                l = mid + 1 # check right side
                print(f"l={l}, r={r}, mid={mid}")
            # heck left side
            else:
                print("else")
                r = mid - 1
                print(f"l={l}, r={r}, mid={mid}")
        return minNum
