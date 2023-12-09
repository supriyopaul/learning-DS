from typing import List
import math

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]
        if not nums: return result
        
        left, right = 0, len(nums)-1
        if left == right:
            if nums[left] == nums[right] == target:
                return [left, right]
            return result
        
        while left <= right:
            mid = left + (right-left)//2
            
            if target > nums[mid]: left = mid+1
            elif target < nums[mid]: right = mid-1
            else:
                if mid == 0 or nums[mid-1] != target:
                    result[0] = mid
                    break
                right = mid-1
        
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right-left)//2
            
            if target > nums[mid]: left = mid+1
            elif target < nums[mid]: right = mid-1
            else:
                if mid == len(nums)-1 or nums[mid+1] != target:
                    result[1] = mid
                    break
                left = mid+1
        
        return result
        

if __name__ == '__main__':
    print(Solution().searchRange(nums = [5,7,7,8,8,10], target = 8)) # [3,4]
    print(Solution().searchRange(nums = [5,7,7,8,8,10], target = 6)) # [-1,-1]
    print(Solution().searchRange(nums = [], target = 0)) # [-1,-1]
    print(Solution().searchRange(nums = [3, 3, 3], target = 3)) # [0,2]
    print(Solution().searchRange(nums = [1, 3, 3], target = 3)) # [1,2]
    print(Solution().searchRange(nums = [1, 1, 3], target = 1)) # [0,1]
    print(Solution().searchRange(nums = [2, 2], target = 3)) # [0,1]