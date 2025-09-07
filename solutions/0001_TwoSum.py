class Solution(object):
    def twoSum(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            if (target - num) in lookup:
                return [i, lookup[(target - num)]] 
            else:
                lookup[num] = i