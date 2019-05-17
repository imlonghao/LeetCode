class Solution:
    def sortedSquares(self, A):
        r = [x * x for x in A]
        r.sort()
        return r
