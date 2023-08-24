from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_dict = {}
        result = []
        for n in nums:
            #import pdb; pdb.set_trace()
            if n not in frequency_dict:
                frequency_dict[n] = 1
            else:
                frequency_dict[n] += 1
        
        sorted_frequency_dict = sorted(frequency_dict.items(), key=lambda x:x[1], reverse=True)[:k]
        return [num for num, freq in sorted_frequency_dict]

if __name__ == "__main__":
    print(Solution().topKFrequent(nums = [1,1,1,2,2,3], k = 2)) # [1,2]
    print(Solution().topKFrequent(nums = [1], k = 1)) # [1]
