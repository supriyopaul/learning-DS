from typing import List
from itertools import combinations

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums: return [[]]
        result = []
        for i in range(len(nums)+1):
            result.extend([list(c) for c in combinations(nums, i)])
        return result


if __name__ == '__main__':
    print(Solution().subsets([1,2,3])) # Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    print(Solution().subsets([0]))