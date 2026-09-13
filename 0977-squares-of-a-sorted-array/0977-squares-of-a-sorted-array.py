class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[0]*n
        i=0
        j=n-1
        k=n-1
        while i<=j:
            if nums[i]*nums[i]>=nums[j]*nums[j]:
                ans[k]=nums[i]*nums[i]
                k-=1
                i+=1
            else:
                ans[k]=nums[j]*nums[j]
                k-=1
                j-=1
        return ans

        