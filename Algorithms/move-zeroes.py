class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
        while 0 in nums:
            nums.remove(0)
        for _ in range(zero_count):
            nums.append(0)
