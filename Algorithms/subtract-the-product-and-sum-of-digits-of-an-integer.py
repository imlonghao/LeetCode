class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        a = None
        b = []
        for i in str(n):
            if a is None:
                a = int(i)
            else:
                a *= int(i)
            b.append(int(i))
        return a - sum(b)
