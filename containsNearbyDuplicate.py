from typing import List
from collections import Counter

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_index_dict = dict()
        for index, num in enumerate(nums):
            if num not in nums_index_dict:
                nums_index_dict[num] = [index]
            else:
                nums_index_dict[num].append(index)

        for num, indices in nums_index_dict.items():
            if len(indices) == 1: continue

            start, end = 0, 1
            while end < len(indices):
                if abs(indices[start]-indices[end]) <= k: return True
                start += 1
                end +=1
        return False
            
if __name__ == "__main__":
    obj = Solution()
    print(obj.containsNearbyDuplicate(nums = [1,2,3,1], k = 3)) # True
    print(obj.containsNearbyDuplicate(nums = [1,0,1,1], k = 1)) # True
    print(obj.containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2)) # False