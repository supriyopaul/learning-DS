from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        max_volume = 0
        while start < end:
            vol = min(height[start], height[end]) * (end - start)
            print(f"{max_volume} {vol}")
            if height[start] > height[end]:
                end = end - 1
            else:
                start = start + 1
            max_volume = max(max_volume,vol)
        return(max_volume)

if __name__ == '__main__':
    print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))# 49
    print(Solution().maxArea([1,1])) # 1