class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        total=0
        for j in range(k):
            total+=arr[j]
        i=0
        count=0
        target=threshold*k
        if total>=target:
            count+=1
        for j in range(k,len(arr)):
            total=total-arr[i]+arr[j]
            i+=1
            if total>=target:
                count+=1
        return count


        