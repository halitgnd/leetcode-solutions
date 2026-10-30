class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        temp=list(nums)
        for j in temp:
            nums.append(j)
        return nums  

        