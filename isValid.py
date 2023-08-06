class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(':')', '[':']', '{':'}'}
        stack = []

        for currBracket in s:
            if currBracket in brackets.keys():
                stack.append(currBracket)
            else:
                if(len(stack) == 0):
                    return False
                bracketPop = brackets[stack.pop()]
                if currBracket != bracketPop:
                    return False

        if(len(stack) == 0):
            return True
        else:
            return False