class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        while True:
            first = nums[0]
            nums.remove(first)
            if first in nums:
                nums.remove(first)
            else:
                return first
