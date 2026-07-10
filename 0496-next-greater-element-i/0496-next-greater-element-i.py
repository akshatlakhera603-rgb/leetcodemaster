class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lis=[]
        dic={}
        for num in nums2:
            while lis and num >lis[-1]:
                small=lis.pop()
                dic[small]=num
            lis.append(num)
        ans=[]
        for num in nums1:
            if num in dic:
                ans.append(dic[num])
            else:
                ans.append(-1)
        return ans
