class Solution:
    def averageValue(self, nums: List[int]) -> int:
        sum=0
        count=0
        for i in range(len(nums)):
            if nums[i]%2==0 and nums[i]%3==0:
                sum+=nums[i]
                count+=1
        if count==0:
            return 0
        else:
            return sum//count
        