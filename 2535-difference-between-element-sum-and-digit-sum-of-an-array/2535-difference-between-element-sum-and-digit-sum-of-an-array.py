class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        temp=0
        temp2=0
        for i in nums:
            temp+=i
        for i in nums:
            while i !=0:
                rem=i%10
                temp2+=rem
                i=i//10
        return temp - temp2
    
        