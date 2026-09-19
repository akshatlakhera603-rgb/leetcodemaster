class Solution:
    def search(self, nums: list[int], target: int) -> int:
        i=0
        high=len(nums)-1
    
        while i<=high:
            mid=(i+high)//2
            if nums[mid]==target:
                return mid
            if nums[i]<=nums[mid]:
                if nums[i]<=target <nums[mid]:
                    high=mid-1
                else:
                    i=mid+1

            else:
                if nums[mid]<target<=nums[high]:
                    i=mid+1
                else:
                    high=mid-1
        return -1
            
    