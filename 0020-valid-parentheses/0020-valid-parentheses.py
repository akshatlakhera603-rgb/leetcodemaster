class Solution:
    def isValid(self, s: str) -> bool:
        if s[0]==")" or s[0]=="}" or s[0]=="]":
            return False
        stack=[]
        mapp={')':'(',']':'[','}':'{'}
        for ch in s:
            if ch in "([{":
                stack.append(ch)
            elif ch in ")]}":
                if not stack or stack[-1]!=mapp[ch]:
                    return False
                stack.pop()
        return len(stack)==0
        return True
        