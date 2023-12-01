from typing import List

class Solution:
    '''

    '''

    def jump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2: return 0

        jumps = 1
        max_reach = nums[0]
        current_max_reach = max_reach

        for i in range(1, n-1):
            if i == n-1: return jumps
            
            max_reach = max(max_reach, i+nums[i])
            
            if i == current_max_reach:
                jumps = jumps+1
                current_max_reach = max_reach
        return jumps

if __name__ == '__main__':
    solution = Solution()
    print(solution.jump([2,3,1,1,4])) # 2
    print(solution.jump([2,3,0,1,4])) # 2
    print(solution.jump([2,1])) # 2