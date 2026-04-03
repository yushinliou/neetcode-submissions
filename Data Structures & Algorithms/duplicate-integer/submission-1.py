class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lenNums = len(nums)
        hashSetNums = set(nums)
        lenHashNums = len(hashSetNums)
        print("hashSetNums", hashSetNums)
        print("lenNums", lenNums)
        if lenHashNums < lenNums:
            return True
        else:
            return False