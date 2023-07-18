from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = list()
        nums1_dict, nums2_dict = dict(), dict()
        for num in nums1:
            if num not in nums1_dict: nums1_dict[num] = 1
            else: nums1_dict[num] += 1
        for num in nums2:
            if num not in nums2_dict: nums2_dict[num] = 1
            else: nums2_dict[num] += 1
        import pdb; pdb.set_trace()
        for num in nums1_dict:
            if num in nums2_dict: result.extend([num]*(min(nums1_dict[num], nums1_dict[num])))

        return result

if __name__ == "__main__":
    sol = Solution()
    #print(sol.intersect(nums1 = [1,2,2,1], nums2 = [2,2]))
    #print(sol.intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))
    print(sol.intersect(nums1 = [1,2,2,1], nums2 = [2]))