class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            another = target - nums[i]
            if another in nums:
                x = nums.index(another)
                if x == i:
                    continue
                return [min(x, i), max(x, i)]
