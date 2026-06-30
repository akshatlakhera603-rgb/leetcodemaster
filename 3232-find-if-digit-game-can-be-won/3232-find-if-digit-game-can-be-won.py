class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        sum=0
        sum2=0
        for i in nums:
            if i>=10:
                sum+=i
            if i<10:
                sum2+=i
        if sum==sum2:
            return False
        else:
            return True        