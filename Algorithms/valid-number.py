class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        allow = '0123456789e.-+'
        s = s.strip()
        if len(s) == 0:
            return False
        for each in [x for x in s]:
            if each not in allow:
                return False
        try:
            float(s)
        except Exception as e:
            return False
        return True
