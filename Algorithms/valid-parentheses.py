class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mapping = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        status = list()
        for i in s:
            if i in mapping.keys():
                status.append(mapping[i])
            elif i in mapping.values() and len(status) == 0:
                return False
            elif i == status[-1]:
                status.pop(-1)
            else:
                return False
        if len(status) == 0:
            return True
        else:
            return False
