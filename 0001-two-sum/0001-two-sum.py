class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        gorulenler = {}  # {sayi: indis}
        
        for i, num in enumerate(nums):
            kalan = target - num
            if kalan in gorulenler:
                return [gorulenler[kalan], i]
            gorulenler[num] = i
        return []
