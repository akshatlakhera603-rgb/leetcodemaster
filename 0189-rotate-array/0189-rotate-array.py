class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        arr=[]
        n=len(nums)
        k=k%n
        for i in range(n-k,n):
            arr.append(nums[i])
        for i in range(0,n-k):
            arr.append(nums[i])
        for i in range(len(arr)):
            nums[i]=arr[i]
        return nums


        