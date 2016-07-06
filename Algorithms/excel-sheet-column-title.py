class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = []
        while n != 0:
            if n % 26 == 0:
                ans.append(26)
                n -= 1
            else:
                ans.append(n % 26)
            n = n / 26
        return ''.join([chr(x + 96) for x in ans[::-1]]).upper()
