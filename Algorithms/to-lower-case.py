class Solution:
    def toLowerCase(self, str: str) -> str:
        s = ""
        for i in str:
            if 'A' <= i <= 'Z':
                s += chr(ord(i)+32)
            else:
                s += i
        return s
