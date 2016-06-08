class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ss = []
        tt = []
        for i in s:
            ss.append(i)
        for i in t:
            tt.append(i)
        ss.sort()
        tt.sort()
        return ss == tt

