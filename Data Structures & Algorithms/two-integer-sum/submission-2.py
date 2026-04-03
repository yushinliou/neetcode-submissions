class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_j_list = {}
        for i, num_i in enumerate(nums):
            num_j = target - num_i
            for j, x in enumerate(nums):
                if j == i:
                    continue
                else:
                    if x == num_j:
                        idx_j = j
                        print(idx_j)
                        return [i, idx_j]



