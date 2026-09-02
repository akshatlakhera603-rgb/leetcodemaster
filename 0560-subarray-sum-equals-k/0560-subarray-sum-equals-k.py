class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        dic={0:1}
        prefixsum=0
        for i in nums:
            prefixsum+=i
            target=prefixsum-k
            if target in dic:
                count+=dic.get(target)
            dic[prefixsum]=dic.get(prefixsum,0)+1
        return count
