class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_price = None
        max_profit = 0

        for price in prices:
            if current_price is None:
                current_price = price
            elif price > current_price:
                max_profit = max(max_profit, price - current_price)
            else:
                current_price = price
        
        return max_profit