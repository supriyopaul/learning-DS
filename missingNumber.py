from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_len = len(nums)
        return sum([i for i in range(0, nums_len+1)]) - sum(nums)

if __name__ == '__main__':
    solution = Solution()

    print(solution.missingNumber([3,0,1]))# == 2
    print(solution.missingNumber([0,1]))# == 2
    print(solution.missingNumber([9,6,4,2,3,5,7,0,1]))# == 8