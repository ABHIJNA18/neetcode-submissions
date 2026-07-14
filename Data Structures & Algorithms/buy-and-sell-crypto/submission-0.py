class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof=0

        for i,price in enumerate(prices):
            if price == max(prices[i:]):
                continue
            else:
                cur_profit=max(prices[i:])-price
            max_prof=max(cur_profit,max_prof)
            
        return max_prof
        