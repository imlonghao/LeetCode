class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        c = 0
        r = ""
        for i in S:
            if i == "(":
                c += 1
                if c > 1:
                    r += i
                    continue
            if i == ")":
                c -= 1
                if c > 0:
                    r += i
                    continue
        return r
