class Solution:
    def checkRecord(self, s: str) -> bool:
        a = 0
        l = 0

        for ch in s:
            if ch == "A":
                a += 1
                l = 0

                if a >= 2:
                    return False

            elif ch == "L":
                l += 1

                if l >= 3:
                    return False

            else:
                l = 0

        return True