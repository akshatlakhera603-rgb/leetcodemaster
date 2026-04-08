class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        if n==3:
            return nums[0]*nums[1]*nums[2]
        product=nums[n-1]*nums[n-2]*nums[n-3]
        product1=nums[0]*nums[1]*nums[n-1]
        product2=max(product,product1)
        return product2

        