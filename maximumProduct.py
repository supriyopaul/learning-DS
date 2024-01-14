from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        sorted_nums  = sorted(nums)
        option1 = sorted_nums[-3:]
        option2 = sorted_nums[0:2]; option2.append((sorted_nums[-1]))
        product1 = 1
        product2 = 1
        print(option1, option2)
        for num1, num2 in zip(option1, option2):
            product1 *= num1
            product2 *= num2

        return max(product1, product2)



if __name__ == "__main__":
    print(Solution().maximumProduct(nums = [1,2,3])) # 6
    print(Solution().maximumProduct(nums = [1,2,3,4])) # 24
    print(Solution().maximumProduct(nums = [-1,-2,-3])) # -6