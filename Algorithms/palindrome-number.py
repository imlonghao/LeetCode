class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = [i for i in str(x)]
        length = len(x) if len(x) % 2 == 0 else len(x) + 1
        for i in range(int(length / 2)):
            if x[i] != x[-(i + 1)]:
                return False
        return True
