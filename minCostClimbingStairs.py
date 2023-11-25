from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        total_cost = 0
        for index in range(len(cost)-2):
            if cost[index] < cost[index+1] + cost[index+2]:
                cur_index = index
            if  cost[index+1] < cost[index] + cost[index+2]:
                cur_index = index+1
            else:
                cur_index = index+2

            total_cost += cost[cur_index]
            index = cur_index

        return total_cost



if __name__ == "__main__":
    print(Solution().minCostClimbingStairs([10,15,20]))
    print(Solution().minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))