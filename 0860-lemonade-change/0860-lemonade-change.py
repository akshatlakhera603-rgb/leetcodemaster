class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        frq = {5: 0, 10: 0}
        for i in bills:
            if i == 5:
                frq[5] += 1
            elif i == 10:
                if frq[5] == 0:
                    return False
                frq[5] -= 1
                frq[10] += 1
            elif i == 20:
                if frq[10] > 0 and frq[5] > 0:
                    frq[10] -= 1
                    frq[5] -= 1
                elif frq[5] >= 3:
                    frq[5] -= 3
                else:
                    return False
        return True