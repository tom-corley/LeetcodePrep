class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        # Use binary search
        # cases: l < m < r, l < m > r, l > m < r, l > m > r
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if m == 0:
                if nums[m] < nums[m+1]:
                    l = m + 1
                else:
                    return 0
            elif m == len(nums) - 1:
                if nums[m] < nums[m-1]:
                    r = m - 1
                else:
                    return m
            else:
                if nums[m] > nums[m+1] and nums[m] > nums[m-1]:
                    return m
                elif nums[m] < nums[m+1]:
                    l = m + 1
                else:
                    r = m -1
        return l