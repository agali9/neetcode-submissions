class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d ={"}":"{","]":"[",")":"("}
        for c in s:
            print(c)
            if c in "([{": stack.append(c)
            else:
                if stack:
                    if d[c] != stack[-1]: return False
                    else: stack.pop()
                else: return False
        return len(stack) == 0