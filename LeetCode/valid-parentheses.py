# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                b = stack.pop()
                if not((b == "(" and c == ")") or (b == "{" and c == "}") or (b == "[" and c == "]")):
                    return False
        if len(stack) > 0:
            return False
        return True
        