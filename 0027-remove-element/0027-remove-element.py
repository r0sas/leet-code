class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        i = 0
        for j in range(0,len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i+=1
        return i