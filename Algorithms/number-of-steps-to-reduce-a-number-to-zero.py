class Solution:
    def numberOfSteps (self, num: int) -> int:
        c = 0
        while num != 0:
            c += 1
            x = num % 2
            if x == 1:
                num -= 1
            else:
                num /= 2
        return c
