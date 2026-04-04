class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '':
            return ''
        window = dict()
        have = 0
        countT = dict()
        need = 0
        res=[-1, -1]
        resLen = float('inf')
        found = False
        l = 0

        for char in t:
            if char in countT:
                countT[char] += 1
            else:
                countT[char] = 1
        
        need = len(countT)

        for r in range(len(s)):
            if s[r] in window:
                window[s[r]] += 1
            else:
                window[s[r]] = 1
            if (s[r] in countT) and (window[s[r]] == countT[s[r]]):
                have += 1
            while(have == need):
                found = True
                if len(s[l:r+1]) < resLen:
                    res = s[l:r+1]
                    resLen = len(res)
                window[s[l]] -= 1
                if s[l] in countT and (window[s[l]] < countT[s[l]]):
                    have -= 1
                l += 1
        if found == False:
            return ""
        return res
        



