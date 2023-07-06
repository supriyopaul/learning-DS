from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap  = []
        for n in nums:
            heapq.heappush(heap, n)
        for i in range(len(nums)-k+1):
            element = heapq.heappop(heap)
        return element

if __name__ == '__main__':
    print(Solution().findKthLargest([3,2,1,5,6,4], k=2)) # 5
    print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6], k=4)) # 4