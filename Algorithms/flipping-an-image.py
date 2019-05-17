class Solution:
    def flipAndInvertImage(self, A):
        l = len(A[0])
        ll = round(l/2)
        for i in range(len(A)):
            t = A[i]
            for ii in range(ll):
                t[ii], t[l-ii-1] = t[l-ii-1], t[ii]
            for ii in range(l):
                if t[ii] == 1:
                    t[ii] = 0
                else:
                    t[ii] = 1
            A[i] = t
        return A
