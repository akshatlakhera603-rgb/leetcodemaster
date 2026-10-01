class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        freq = {}
        for x in hand:
            freq[x] = freq.get(x, 0) + 1
        hand.sort()
        for x in hand:
            if freq[x] == 0:
                continue
            for j in range(x, x + groupSize):
                if freq.get(j, 0) == 0:
                    return False
                freq[j] -= 1
        return True