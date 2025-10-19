class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = int(len(nums)/2)
        idx = 0
        if target <= nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)
        while i > 0:
            if target > nums[i]:
                nums = nums[i:]
                idx +=i
            elif target < nums[i]:
                nums = nums[:i]
            else:
                idx += i
                return idx
            i = int(len(nums)/2)
        return idx +1