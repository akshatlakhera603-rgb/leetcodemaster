class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonal={}
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                d=i+j
                if d not in diagonal:
                    diagonal[d]=[]
                diagonal[d].append(nums[i][j])
        for d in diagonal:
            diagonal[d].reverse()
        ans=[]
        for d in sorted(diagonal):
            ans.extend(diagonal[d])
        return ans

                

        