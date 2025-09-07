from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        lprod = 1
        rprod = 1

        for i in range(1, len(nums)):
            lprod *= nums[i-1]
            ans[i] *= lprod
        
        for i in range(len(nums) - 2, -1, -1):
            rprod *= nums[i+1]
            ans[i] *= rprod

        return ans

    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        unique = set()
        for num in nums:
            unique.add(num)
        if len(unique) == 1 and 1 in unique:
            return [1] * len(nums)


        # Build prefixes
        prefixes = [1]
        product = 1
        rv_product = 1
        suffixes = [1]
        for i in range(1, len(nums)):
            product *= nums[i-1]
            rv_product *= nums[-1-(i-1)]
            prefixes.append(product)
            suffixes = [rv_product] + suffixes

        ans = []
        for i in range(len(nums)):
            ans.append(prefixes[i] * suffixes[i])
        return ans

    def productExceptSelf3(self, nums: List[int]) -> List[int]:
        # Setup
        ans = [1] * len(nums)
        lprod = 1
        rprod = 1
        
        # Prefixes
        for i in range(1, len(nums)):
            lprod *= nums[i-1]
            ans[i] *= lprod

        # Suffixes 
        for i in range(1, len(nums)):
            rprod *= nums[-1-(i-1)]
            ans[-1-i] *= rprod

        return ans