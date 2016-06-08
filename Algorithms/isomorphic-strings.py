class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        replaced = {}
        s = [x for x in s]
        t = [x for x in t]
        for i in range(len(s)):
            if replaced.get(s[i]):
                if replaced[s[i]] != t[i]:
                    return False
            else:
                if t[i] in replaced.values():
                    return False
            replaced[s[i]] = t[i]
        return True
