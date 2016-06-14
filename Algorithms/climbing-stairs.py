class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 1
        last = 0
        for _ in range(n):
            tmp = ret
            ret += last
            last = tmp
        return ret
