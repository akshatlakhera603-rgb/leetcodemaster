class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        arr=[0]*n
        for i in range(len(arr)):
            arr[i]=start+2*i
        result=0
        for i in arr:
            result^=i
        return result
        