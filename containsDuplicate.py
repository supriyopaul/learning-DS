from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        for num in nums:
            if num not in nums_set:
                nums_set.add(num)
            else: return True
        return False

if __name__ == "__main__":
    print(Solution().containsDuplicate( nums = [1,2,3,1])) # True
    print(Solution().containsDuplicate(nums = [1,2,3,4])) # False
    print(Solution().containsDuplicate(nums = [1,1,1,3,3,4,3,2,4,2])) # True