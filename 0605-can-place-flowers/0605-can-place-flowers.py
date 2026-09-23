class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if n==0:
            return True
        for i in range (len(flowerbed)):
            if flowerbed[i]==1:
                continue
            else:
                if i!=0 and i!=len(flowerbed) -1:
                    if flowerbed[i-1]==0 and flowerbed[i+1]==0:
                        flowerbed[i]=1
                        n-=1
                elif i==0:
                    if len(flowerbed)==1 or flowerbed[i+1]==0:
                        flowerbed[i]=1
                        n-=1
                elif i==len(flowerbed)-1:
                    if flowerbed[i-1]==0:
                        flowerbed[i]=1
                        n-=1
            if n==0:
                return True
        return  False
        