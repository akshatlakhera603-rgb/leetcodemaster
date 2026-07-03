class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curentsum=0
        for j in range(k):
            curentsum+=nums[j]
        i=0
        maxsum=curentsum
        for j in range(k,len(nums)):
            curentsum=curentsum-nums[i]+nums[j]
            maxsum=max(maxsum,curentsum)
            i+=1
        return maxsum/k

        

        