class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3=[]
        i=0
        j=0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                nums3.append(nums1[i])
                i+=1
            else:
                nums3.append(nums2[j])
                j+=1

        while i<len(nums1):
            nums3.append(nums1[i])
            i+=1
        while j<len(nums2):
            nums3.append(nums2[j])
            j+=1
        low=0
        high=len(nums3)-1
        ans=0
        if len(nums3)%2!=0:
            mid=(low+high)//2
            ans=nums3[mid]
        else:
            mid=(low+high)//2
            ans=(nums3[mid]+nums3[mid+1])/2
        return ans

            
        
        