class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        sayac = 0
        max_sayac = 0
        
        for i in nums:
            if i == 1:
                sayac += 1
                if sayac > max_sayac:
                    max_sayac = sayac
            else:
                sayac = 0
                
        return max_sayac