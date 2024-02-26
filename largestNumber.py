from typing import List
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(a, b):
            if a+b <= b+a:
                return -1
            else:
                return 1
        
        nums_str = [str(n) for n in nums]
        nums_str.sort(key=cmp_to_key(compare), reverse=True)

        return str(int("".join(nums_str)))

if __name__ == "__main__":
    obj = Solution()
    print(obj.largestNumber(nums=[10, 2]))  # 210
    print(obj.largestNumber(nums=[3, 30, 34, 5, 9]))  # 9534330
    print(obj.largestNumber(nums=[1, 2, 3, 1, 2, 3]))  #332211
    print(obj.largestNumber(nums=[1, 0, 0]))  # 100
    print(obj.largestNumber(nums=[10,2,9,39,17]))  # 93921710
