class Solution(object):
    def twoSum(self, nums, target):
        pair_nums = {}            

        for i, num in enumerate(nums):
            if target - num in pair_nums:
                return [i, pair_nums[target-num]]
            pair_nums[num] = i