class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        odd=0
        even=0
        n=len(nums)
        answer=[0]*n
        for num in nums:
            if num%2==0:
                even+=1
            else:
                odd+=1
        for i in range(len(nums)):
            if nums[i]%2==0:
                even-=1
                answer[i]=odd
            else:
                odd-=1
                answer[i]=even
        return answer


        

        