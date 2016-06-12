class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return [1]
        if digits[-1] % 10 == 9:
            ret = list()
            for x in self.plusOne(digits[:-1]):
                ret.append(x)
            ret.append(0)
            return ret
        else:
            return digits[:-1] + [digits[-1] + 1]
