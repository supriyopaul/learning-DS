from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = i = 0
        right = len(nums)-1

        while i <= right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                

            elif nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
                continue

            i += 1
            
        return nums

if __name__ == "__main__":
    print(Solution().sortColors([2,0,2,1,1,0]))
    print(Solution().sortColors([2,0,1]))
    print(Solution().sortColors([1,0,1]))
    print(Solution().sortColors([0,1,0]))