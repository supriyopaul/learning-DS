from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        consecutive = 0
        max_consecutive = 0
        
        visited = set()
        for i, num in enumerate(nums):
            if (num-1) not in nums_set and num not in visited:
                start = num
                visited.add(start)
                consecutive += 1

                while True:
                    if start+1 in nums_set:
                        consecutive += 1
                        visited.add(start+1)
                        start = start + 1
                    else:
                        max_consecutive = max(max_consecutive, consecutive)
                        consecutive = 0
                        break
            
        return max_consecutive

        
if __name__ == "__main__":
    print(Solution().longestConsecutive([100,4,200,1,3,2])) # 4
    print(Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1])) # 9
    print(Solution().longestConsecutive([0,-1])) # 9