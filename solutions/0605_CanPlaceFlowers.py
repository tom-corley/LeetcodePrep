from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i, plot in enumerate(flowerbed):
            if ((i > 0) and flowerbed[i-1]) or plot or ((i < len(flowerbed) - 1) and flowerbed[i+1]):
                continue
            else:
                flowerbed[i] = 1
                n -= 1
        return n <= 0