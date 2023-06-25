class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_nums = sorted(list(set(nums)))
        # nums = [1,1,2] & unique_nums = [1,2]
        for i in range(len(nums)) :
            if i < len(unique_nums): nums[i] = unique_nums[i]
            else: nums[i] = 0
        return len(unique_nums)

if __name__ == "__main__":
    print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))