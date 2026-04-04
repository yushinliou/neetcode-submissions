class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        left = 0
        right = 1
        subS = s[left]
        maxS = s[left]
        while(right < len(s)):
            print(f"check {s[right]}")
            if s[right] not in subS:
                print(f"{s[right]} not in {subS}")
                subS = s[left:right+1]
                print(f"s[left:right]={s[left:right+1]}, l={left}, r={right}")
                if len(subS) > len(maxS):
                    maxS = subS
                    print(f"maxS={maxS}")
            else: # if in substring, left jump to the position of that char +1
                print(print(f"{s[right]} in {subS}"))
                while(s[left] != s[right]):
                    print(f"move left to {s[left]}, left={left}")
                    left += 1
                print(f"move left to {s[left]}, left={left}")
                left += 1
                print(f"final l={left}")
                subS = s[left:right+1]
            right += 1
        print(f"maxS={maxS}")
        return len(maxS)