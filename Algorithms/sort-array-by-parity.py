class Solution:
    def sortArrayByParity(self, A: list) -> list:
        e = []
        o = []
        for i in A:
            if i % 2 == 0:
                e.append(i)
            else:
                o.append(i)
        return e + o