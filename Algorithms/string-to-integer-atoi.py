class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        allow = '0123456789.-+'
        num = ''
        str = str.lstrip()
        for i in [x for x in str]:
            if i in allow:
                num += i
            else:
                break
        try:
            ret = int(float(num))
            if ret > 2147483647:
                return 2147483647
            elif ret < -2147483648:
                return -2147483648
            return ret
        except:
            return 0
