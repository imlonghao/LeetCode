class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            x = '-' + str(x)[:0:-1]
        else:
            x = str(x)[::-1]
        try:
            x = int(x.lstrip('0'))
        except ValueError:
            return 0
        if x < pow(-2, 31) - 1 or x > pow(2, 31) - 1:
            return 0
        return x
