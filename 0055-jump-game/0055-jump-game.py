class Solution:
    def canJump(self, nums: List[int]) -> bool:
        fartherst=nums[0]
        if len(nums)==1:
            return True
        for i in range (1,len(nums)):
            if i > fartherst:
                return False
            fartherst=max(fartherst,i+nums[i])
            if fartherst >=len(nums)-1:
                return True
        