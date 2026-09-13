class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ans=1
        for i in nums:
            ans*=i
        def signFunc(result):
            if result>0:
                return 1
            elif result<0:
                return -1
            else:
                return 0
        
        return signFunc(ans)
        
        