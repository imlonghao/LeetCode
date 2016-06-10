class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        ret = 0
        word = dict()
        for i in range(len(s)):
            if s[i] in word and word[s[i]] >= left:
                ret = max(ret, i - left)
                left = word[s[i]] + 1
            word[s[i]] = i
        ret = max(ret, len(s) - left)
        return ret
