class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return [(i, nums.index(target - nums[i], i+1)) for i in range(len(nums)) if (target - nums[i]) in nums[i+1:]][0]