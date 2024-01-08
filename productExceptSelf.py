from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            answer[i] = prefix
            prefix = prefix * nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            answer[i] *= postfix
            postfix = postfix * nums[i]
        return answer

if __name__ == "__main__":
    print(Solution().productExceptSelf(nums = [1,2,3,4])) # [24,12,8,6]
    print(Solution().productExceptSelf(nums = [-1,1,0,-3,3])) # [0,0,9,0,0]
