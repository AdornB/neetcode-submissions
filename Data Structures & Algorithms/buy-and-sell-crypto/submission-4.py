class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        best = 0

        for price in prices:
            if price < buy:
                buy = price
            elif price-buy > best:
                best = price-buy
        return best