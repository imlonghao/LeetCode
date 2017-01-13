class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        index = 0
        up = True
        l = [[] for _ in range(numRows)]
        for i in range(len(s)):
            l[index].append(s[i])
            if numRows == 1:
                continue
            if index == 0 or index == numRows - 1:
                up = not up
            if up:
                index -= 1
            else:
                index += 1
        ans = ''
        for i in l:
            ans += ''.join(i)
        return ans
