class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans_lst = []
        zero_pos_lst = []
        all_product = 1
        for i, num in enumerate(nums):
            if num == 0:
                zero_pos_lst.append(i)
                continue
            all_product = all_product * num
        if len(zero_pos_lst) >= 2:
            for num in nums:
                ans_lst.append(0)
        elif len(zero_pos_lst) == 1:
            for num in nums:
                ans_lst.append(0)
            ans_lst[zero_pos_lst[0]] = all_product
        else:
            for i, num in enumerate(nums):
                ans_lst.append(int(all_product / num))
        return ans_lst
            


