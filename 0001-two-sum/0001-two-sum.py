class Solution(object):
    def twoSum(self, nums, target):
        dic={}
        for i in range(0,len(nums)):
            comp=target-nums[i]
            if comp in dic:
                return [dic[comp],i]
            dic[nums[i]]=i
        
