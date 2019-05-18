class Solution:
    def maxIncreaseKeepingSkyline(self, grid) -> int:
        s = 0
        tb = []
        lr = []
        gridr = list(map(list, zip(*grid)))
        for i in gridr:
            tb.append(max(i))
        for i in grid:
            lr.append(max(i))
        for x in range(len(tb)):
            for y in range(len(lr)):
                c = grid[y][x]
                s += min(tb[x], lr[y]) - c
        return s
