class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count=0
        prefixsum=0
        dic={0:1}
        for i in nums:
            prefixsum+=i
            if prefixsum-goal in dic:
                count+=dic[prefixsum-goal]
            dic[prefixsum]=dic.get(prefixsum,0)+1
        return count