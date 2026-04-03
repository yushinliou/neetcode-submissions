class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums_set = set(nums)
        current_len = 1
        max_len = 1
        for num in nums_set:
            if (num - 1) not in nums_set:
                current_len = 1
                while (num + current_len) in nums_set:
                    current_len += 1
                    max_len = max(current_len, max_len)

        return max_len