from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Iterate over j, hash values on left
        nums.sort()
        print(nums)
        ans = []
        triplets = set()
        leftset = set()
        leftset.add(nums[0])
        for j in range(1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if -(nums[j] + nums[k]) in leftset and (-(nums[j] + nums[k]), nums[j], nums[k]) not in triplets:
                    ans.append([-(nums[j] + nums[k]), nums[j], nums[k]])
                    triplets.add((-(nums[j] + nums[k]), nums[j], nums[k]))
            leftset.add(nums[j])
        return ans