class Solution:
    def simplifyPath(self, path: str) -> str:
        arr=list(path.split("/"))
        stack=[]
        for i in arr:
            if i =='' or i ==".":
                continue
            if i=="..":
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        ans=''
        for i in stack:
            ans+="/"+i
        return "/" if ans=='' else ans

        