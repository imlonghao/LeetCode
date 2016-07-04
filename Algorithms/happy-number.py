class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        loop = []
        while True:
            if n in loop or n < 0:
                return False
            if n == 1:
                return True
            loop.append(n)
            n = sum([int(x) ** 2 for x in str(n)])
