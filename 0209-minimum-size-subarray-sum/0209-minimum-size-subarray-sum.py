class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low=0
        currentsum=0
        minlength=float('inf')
        for high in range(len(nums)):
            currentsum+=nums[high]
            while currentsum>=target:
                minlength=min(minlength,high-low+1)
                currentsum-=nums[low]
                low+=1
        return 0 if minlength==float('inf') else minlength

        