class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count=0

        for i in range(1,len(nums)):
            while nums[i]<=nums[i-1]:
                need=nums[i-1]-nums[i]+1
                nums[i]+=need
                count+=need
                

        return count
        