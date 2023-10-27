from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = {0:0, 1:0, 2:0}
        
        for num in nums:
            counts[num] += 1
        
        nums = []
        for num, count in counts.items():
            nums.extend([num]*count)


if __name__ == "__main__":
    print(Solution().sortColors([2,0,2,1,1,0]))
    print(Solution().sortColors([2,0,1]))