class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        lis=[]
        dic={}
        n=len(nums)
        for i in range(2*n):
            i%=n
            while lis and nums[i] >nums[lis[-1]]:
                small=lis.pop()
                
                dic[small]=nums[i]
            if len(lis) <n:
                lis.append(i)
        ans=[]
        for i in range(n):
            if i in dic:

                ans.append(dic[i])
            else:
                ans.append(-1)
        
        return ans
