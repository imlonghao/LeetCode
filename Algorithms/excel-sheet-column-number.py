class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = [x for x in s.lower()][::-1]
        for i in range(len(s)):
            s[i] = 26 ** i * (ord(s[i]) - 96)
        return sum(s)
