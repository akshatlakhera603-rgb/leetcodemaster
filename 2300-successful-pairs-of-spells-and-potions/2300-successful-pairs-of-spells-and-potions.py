class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n=len(potions)
        potions.sort()
        ans=[]
        for x in range(len(spells)):
            i=0
            j=n-1
            while i<=j:
                mid=(i+j)//2
                if spells[x]*potions[mid]>=success:
                    j=mid-1
                else:
                    i=mid+1
            ans.append(n-i)
        return ans

        