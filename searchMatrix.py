from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        num_rows = len(matrix) - 1
        num_cloumns = len(matrix[0]) - 1

        left, right = 0, num_rows
        mid = (left+right)//2
        while left <= right:
            print(left, right, mid)
            if target == matrix[mid][0]:
                return True
            elif target < matrix[mid][0]:
                right = mid - 1
            else:
                left = mid + 1
            mid = (left+right)//2
        
        row = mid
        left, right = 0, num_cloumns
        mid = (left+right)//2
        while left <= right:
            print(left, right, mid)
            if target == matrix[row][mid]:
                return True
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                left = mid + 1
            mid = (left+right)//2
        return False


if __name__ == '__main__':
    print(Solution().searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3)) # true
    print(Solution().searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13)) # false
    print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 11)) # true
    