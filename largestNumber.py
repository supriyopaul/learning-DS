from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        """
        Approach 1 - Simple Sort
        1. Convert each number in nums to a string
           input: [3, 30, 34, 5, 9]
           output: ['3', '30', '34', '5', '9']

        2. Sort them in descending order
           input: ['3', '30', '34', '5', '9']
           output: ['9', '5', '34', '30', '3']

        3. Concatenate the sorted list of strings
           input: ['9', '5', '34', '30', '3']
           output: '9534303'

        4. Convert it to an int
           input: '9534303'
           output: 9534303
        """
        # def simple_sort(nums):
        #     nums_str = sorted([str(n) for n in nums], reverse=True)
        #     return str(int(''.join(nums_str)))
        # This approach fails in cases like ['3', '30']
        # This approach fails because it does not consider the best combination when 
        # numbers are concatenated. For example, '30' should come after '3' for a larger number.

        """
        Approach 2 - Divide and Conquer
        1. Divide the array into halves until there is just 1 element remaining
           input: [3, 30, 34, 5, 9]
           output: Step1: [3, 30, 34, 5, 9] -> [3, 30], [34, 5, 9]
                   Step 2: [3, 30] -> [3], [30] | [34, 5, 9] -> [34], [5, 9]
                   Step 3: [3], [30] | [34] | [5], [9]
                   Final step: [3], [30], [34], [5], [9]

        2. Conquer (Sorting Each Half and Combining)
           Combine two halves such that left+right (option1) or right+left (option2)
           yield the maximum when joined.
           input: [3], [30]
           output: [330]
           input: [34], [5]
           output: [534]
           input:
           [534], [9]
           output: [9534]
           input: [9534], [330]
           output: [9534330]
        """
        # def divide_and_conquer(nums):
        #     def divide(nums):
        #         if len(nums) <= 1:
        #             return nums
        #         mid = len(nums) // 2
        #         left = divide(nums[:mid])
        #         right = divide(nums[mid:])
        #         return merge(left, right)
        #     
        #     def merge(left, right):
        #         option1 = str(left[0]) + str(right[0])
        #         option2 = str(right[0]) + str(left[0])
        #         return [max(option1, option2, key=int)]
        #     
        #     result = divide([str(n) for n in nums])
        #     return str(int(''.join(result)))
        # This approach fails for inputs like [1,2,3,1,2,3] (output would be [321321])
        """
        Approach 3 - Combine Approach 1 and 2
        1. Convert each number in nums to a string and then sort them in descending order
           so that numbers starting with the same digit are grouped together.
           input: [3, 30, 34, 5, 9]
           output: ['3', '30', '34', '5', '9']

        2. Divide the sorted array into halves until there is just 1 element remaining.
           input: ['3', '30', '34', '5', '9']
           output: Step1: ['3', '30', '34', '5', '9'] -> ['3', '30'], ['34', '5', '9']
                   ...
           Final step: ['3'], ['30'], ['34'], ['5'], ['9']

        3. Conquer (Sorting Each Half and Combining)
           Combine two halves such that left+right (option1) or right+left (option2)
           yield the maximum when joined.
           input: ['3'], ['30']
           output: ['330']
           ...
           input: ['9534'], ['330']
           output: ['9534330']
        """
        def divide(nums):
             nums_str = sorted([str(n) for n in nums], reverse=True)
             nums = [int(n) for n in nums_str]
             if len(nums) <= 1:
                return nums
             mid = len(nums) // 2
             left = divide(nums[:mid])
             right = divide(nums[mid:])
             return merge(left, right)
             
        def merge(left, right):
                 option1 = str(left[0]) + str(right[0])
                 option2 = str(right[0]) + str(left[0])
                 return [max(option1, option2, key=int)]
             
        result = divide([str(n) for n in nums])
        return str(int(''.join(result)))

if __name__ == "__main__":
    obj = Solution()
    print(obj.largestNumber(nums=[10, 2]))  # 210
    print(obj.largestNumber(nums=[3, 30, 34, 5, 9]))  # 9534330
    print(obj.largestNumber(nums=[1, 2, 3, 1, 2, 3]))  #332211
    print(obj.largestNumber(nums=[1, 0, 0]))  # 100
    print(obj.largestNumber(nums=[10,2,9,39,17]))  # 93921710
