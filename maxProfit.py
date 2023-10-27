from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        profit = 0
        while right < len(prices):
            print(left, right, profit)
            if prices[right] <= prices[left]:
                left = right
                right = right + 1
            elif prices[right] > prices[left]:
                profit = profit + (prices[right] - prices[left])
                left = right
                right = right + 1
            
        return profit

if __name__ == "__main__":
    print(Solution().maxProfit([7,1,5,3,6,4]))
    print(Solution().maxProfit([1,2,3,4,5]))
    print(Solution().maxProfit([7,6,4,3,1]))