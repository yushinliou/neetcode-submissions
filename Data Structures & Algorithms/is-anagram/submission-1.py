class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sSet = set(list(s))
        tSet = set(set(list(t)))
        if len(s) != len(t):
            return False
        elif sSet == tSet:
            sFreq = {}
            tFreq = {}
            for char in sSet:
                if s.count(char) != t.count(char):
                    return False
            return True
        else:
            return False
            # Sset = set(list(s))tSet = set(list(t))
