class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while True:
            i = []
            for x in str(num):
                i.append(int(x))
            if len(i) == 1:
                return i[0]
            num = 0
            for xx in i:
                num += xx

