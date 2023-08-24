from typing import List

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        for i in range(len(nums)):
            for j in range

        

if __name__ == "__main__":
    print(Solution().findSubsequences([4,6,7,7])) # Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
    print(Solution().findSubsequences([4,4,3,2,1])) # Output: [[4,4]]