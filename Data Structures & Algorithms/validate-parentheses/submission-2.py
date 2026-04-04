class Solution:
    def isValid(self, s: str) -> bool:
        stackLeft = []
        stackRight = []
        bracketSetLeft = set(['(', '{', '['])
        bracketSetRight = set([')', '}', ']'])
        for char in s:
            print(stackLeft)
            if char in bracketSetLeft:
                stackLeft += char
            if char in bracketSetRight:
                if len(stackLeft) == 0:
                    return False
                if (stackLeft[-1] == '(') and (char == ')'):
                    print(f"before cut {stackLeft}")
                    stackLeft = stackLeft[0:-1]
                    print(f"after cut {stackLeft}")
                elif (stackLeft[-1] == '[') and (char == ']'):
                    print(f"before cut {stackLeft}")
                    stackLeft = stackLeft[0:-1]
                    print(f"after cut {stackLeft}")
                elif (stackLeft[-1] == '{') and (char == '}'):
                    print(f"before cut {stackLeft}")
                    stackLeft = stackLeft[0:-1]
                    print(f"after cut {stackLeft}")
                else:
                    print(f"return false in {char}")
                    return False
        print(f"final stackLeft {stackLeft}")
        if len(stackLeft) > 0:
            return False
        return True
            