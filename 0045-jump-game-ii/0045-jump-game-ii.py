class Solution:
    def jump(self, nums: list[int]) -> int:
        jump=0
        currentend=0
        fartherest=0
        for i in range(len(nums)-1):
            fartherest=max(fartherest,i+nums[i])
            if i==currentend:
                jump+=1
                currentend=fartherest
        return jump
        