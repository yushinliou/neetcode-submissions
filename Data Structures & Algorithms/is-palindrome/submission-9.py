class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_s = ""
        # 65–90 for uppercase (A–Z) and 97–122 for lower
        for char in s:
            print(char, ord(char))
            if char.isalnum():
                alpha_s += char.lower()
        if len(alpha_s) == 1:
            return True
        for i in range(int(len(alpha_s)//2)):
            if alpha_s[i] == alpha_s[len(alpha_s)-i-1]:
                print(f"{alpha_s[i]} == {alpha_s[len(alpha_s)-i-1]}")
                continue
            else:
                return False
        return True
        # # if odd
        # for (len(alpha_s) // 2)


