class Solution:
    def sumAndMultiply(self, n: int) -> int:

        s=list(str(n))
        concate=""
        summ=0
        for i in s:
            if i!="0":
                concate+=i
                summ+=int(i)
        if concate == "":
            return 0
        concate=int(concate)
        return concate*summ


        