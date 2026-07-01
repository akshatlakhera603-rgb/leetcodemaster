class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum=prices[0]
        maxprofit=0
        for i in range(len(prices)):
            minimum=min(minimum,prices[i])
            profit=prices[i]-minimum
            maxprofit=max(maxprofit,profit)
        return maxprofit