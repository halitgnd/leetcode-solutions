class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        last_list = []
        for j in range(n):
            last_list.append(nums[j])      # x elemanı: nums[0], nums[1], nums[2]
            last_list.append(nums[j + n])  # y elemanı: nums[3], nums[4], nums[5]
        return last_list


        