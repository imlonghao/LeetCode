class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        length = len(nums1) + len(nums2)
        nums = nums1 + nums2
        nums.sort()
        if length % 2 == 1:
            return nums[(length - 1) / 2]
        else:
            return (float(nums[length / 2]) + float(nums[length / 2 - 1])) / 2
