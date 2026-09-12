class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        suffix = [0] * n
        prefix = [0] * n
        prefix[0]=1
        suffix[n-1]=1

        for i in range(0,n- 1):
            prefix[i+1] = prefix[i] * nums[i]
        for i in range(n-2,-1,-1):
            suffix[i]=suffix[i+1]*nums[i+1]
        result=[0]*n
        for i in range(n):
            result[i]=prefix[i]*suffix[i]
        return result


        