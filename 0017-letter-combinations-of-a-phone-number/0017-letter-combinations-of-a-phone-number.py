class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if digits=="":
            return []
        ma={"2":"abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz"}
        ans=[""]
        for i in digits:
            new=[]
            for j in ans:
                for ch in ma[i]:
                    new.append(j+ch)
            ans=new
        return ans

        