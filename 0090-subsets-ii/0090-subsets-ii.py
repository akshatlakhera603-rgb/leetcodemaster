class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        def solve(i,curr):
            if i == len(nums):
                ans.append(curr.copy())
                return
            curr.append(nums[i])
            solve(i+1,curr)
            curr.pop()
            while i+1 <len(nums) and nums[i]==nums[i+1]:
                i+=1
            
            solve(i+1,curr )
        solve(0,[])
        return ans
        