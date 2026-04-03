class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lenNums = len(nums)
        hashSetNums = set(nums)
        lenHashNums = len(hashSetNums)
        if lenHashNums < lenNums:
            return True
        else:
            return False