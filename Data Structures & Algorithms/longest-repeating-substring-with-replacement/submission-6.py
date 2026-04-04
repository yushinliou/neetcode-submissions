class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = dict()
        l = 0
        maxf = 0
        res = 0
        for r in range(len(s)):
            if (s[r] in count) and (count[s[r]] > 0):
                count[s[r]] += 1
            else:
                count[s[r]] = 1
            maxf = max(maxf, count[s[r]])
            while ((r - l + 1) - (maxf)) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            print(f"curr window: {s[l:r+1]}")
        return res





