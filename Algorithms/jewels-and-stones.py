class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        s = 0
        for i in J:
            s += S.count(i)
        return s
