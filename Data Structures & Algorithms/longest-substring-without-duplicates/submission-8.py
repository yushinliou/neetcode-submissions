class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        left = 0
        right = 1
        # subS = s[left:right+1]
        
        subS_set = set(s[left])
        maxS = s[left]
        while(right < len(s)):
            if s[right] not in subS_set:
                print(f"{s[right]} not in {subS_set}")
                subS_set.add(s[right])
                if len(subS_set) > len(maxS):
                    maxS = subS_set.copy()
                print(f"update maxS={maxS}, subS={subS_set}")
            else:
                print(f"s[right]={s[right]} in {subS_set}")
                while(s[left] != s[right]):
                    print(f"{s[right]} != {s[left]}")
                    print(f"move left to l={left}, {s[left]}")
                    subS_set.remove(s[left])
                    left += 1
                    
                left += 1
                print(f"final left={left}, s[left]={s[left]}")
                print(f"maxS={maxS}, subS={subS_set}")
            right += 1
        return len(maxS)






















        # if len(s) <= 1:
        #     return len(s)
        # left = 0
        # right = 1
        # subS = s[left]
        # maxS = s[left]
        # while(right < len(s)):
        #     print(f"check {s[right]}")
        #     if s[right] not in subS:
        #         print(f"{s[right]} not in {subS}")
        #         subS = s[left:right+1]
        #         print(f"s[left:right]={s[left:right+1]}, l={left}, r={right}")
        #         if len(subS) > len(maxS):
        #             maxS = subS
        #             print(f"maxS={maxS}")
        #     else: # if in substring, left jump to the position of that char +1
        #         print(print(f"{s[right]} in {subS}"))
        #         while(s[left] != s[right]):
        #             print(f"move left to {s[left]}, left={left}")
        #             left += 1
        #         print(f"move left to {s[left]}, left={left}")
        #         left += 1
        #         print(f"final l={left}")
        #         subS = s[left:right+1]
        #     right += 1
        # print(f"maxS={maxS}")
        # return len(maxS)        