from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_k, max_k = 1, max(piles)
        left, right = 1, max_k
        min_k = float('inf')
        #print(k_range)

        while left <= right:
            hours_taken  = 0
            k = (left+right)//2

            for pile in piles:
                hours_to_eat_pile = math.ceil(pile/k)
                hours_taken += hours_to_eat_pile
                #print(f"k = {k}, pile={pile}, hours taken = {hours_taken}")
            if hours_taken <= h:
                right = k - 1
                min_k = k
            elif hours_taken > h:
                left = k + 1
                
        return min_k            
                    
if __name__ == '__main__':
    print(Solution().minEatingSpeed(piles = [3,6,7,11], h = 8)) # 4
    print(Solution().minEatingSpeed(piles = [30,11,23,4,20], h = 5)) # 30
    print(Solution().minEatingSpeed(piles = [30,11,23,4,20], h = 6)) # 23