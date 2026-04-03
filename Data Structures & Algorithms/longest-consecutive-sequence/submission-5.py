class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        else:
            current_lst = []
            max_lst = []
            nums = sorted(list(set(nums)))
            print("after sort:", nums)
            for i, num in enumerate(nums):
                if len(current_lst) == 0:
                    current_lst.append(num)
                    if len(current_lst) > len(max_lst):
                        max_lst = current_lst
                    continue
                if num == (current_lst[-1] + 1):
                    current_lst.append(num)
                    if len(current_lst) > len(max_lst):
                        max_lst = current_lst
                else:
                    current_lst = [num]
        print(max_lst)
        return len(max_lst)