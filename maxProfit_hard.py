from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        left_profits = []
        _max_profit = 0
        max_price = prices[::-1][0]
        right_profits = []

        for price, _price in zip(prices, reversed(prices)):
            max_profit = max(max_profit, (price - min_price))
            left_profits.append(max_profit)
            min_price = min(min_price, price)
        #for _price in reversed(prices):
            _max_profit = max(_max_profit, (max_price - _price))
            right_profits.append(_max_profit)
            max_price = max(max_price, _price)
        right_profits = right_profits[::-1]

        max_profit = 0
        for index in range(len(prices)):
            profit = max(left_profits[0:index+1]) + max(right_profits[index:len(prices)+1])
            max_profit  = max(max_profit, profit)
        return max_profit

if __name__ == "__main__":
    print(Solution().maxProfit([3,3,5,0,0,3,1,4]))
    print(Solution().maxProfit([1,2,3,4,5]))
    print(Solution().maxProfit([7,6,4,3,1]))
    print(Solution().maxProfit([1,2,4,2,5,7,2,4,9,0]))