from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_day = 0
        sell_day = 1
        num_days = len(prices)
        while sell_day < num_days:
            if prices[buy_day] >= prices[sell_day]:
                buy_day = sell_day
                sell_day = sell_day + 1
            else:
                max_profit = max(prices[sell_day]-prices[buy_day], max_profit)
                sell_day = sell_day + 1
        return max_profit

if __name__ == "__main__":
    print(Solution().maxProfit([7,1,5,3,6,4]))
    print(Solution().maxProfit([1,2,3,4,5]))
    print(Solution().maxProfit([7,6,4,3,1]))