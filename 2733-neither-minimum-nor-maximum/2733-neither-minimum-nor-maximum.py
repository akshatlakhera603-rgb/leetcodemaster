class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)<3:
            return -1
        i=0
        j=len(nums)
        for i in range(len(nums)):
            if i+1==len(nums)+1:
                return -1
            else:
                return nums[i+1]

        