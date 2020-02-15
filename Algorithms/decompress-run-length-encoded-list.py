class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        c = []
        for i in range(0, len(nums), 2):
            c += [nums[i+1]] * nums[i]
        return c
