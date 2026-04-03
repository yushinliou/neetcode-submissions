class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans_lst = list()
        nums_no_ij = list()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)-1):
                print("in loop")
                nums_no_ij = nums.copy()
                nums_no_ij.pop(i)
                nums_no_ij.pop(j-1)
                if -(nums[i] + nums[j]) in nums_no_ij:
                    ans_ele = sorted(list((nums[i], nums[j], -(nums[i]+nums[j]))))
                    if ans_ele not in ans_lst:
                        ans_lst.append(ans_ele)
        return ans_lst