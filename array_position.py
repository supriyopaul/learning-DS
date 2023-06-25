'''
Given an array of numbers and a target number X, find the first and last positions of X in the array.

Arr=[1,2,3,4,1,2,7,2,8,9], X=2 -> [1,7]
Arr=[], X=2 -> [-1,-1]
Arr=[1,2,3], X=2 -> [1,1]
'''

class Solution():
    def __init__(self, arr, x):
        self.arr = arr
        self.x = x

    def find_positions(self):
        first_pos = -1
        last_pos = -1
        for index, value in enumerate(self.arr):
            if value == self.x and first_pos == -1:
                first_pos = index
            if value == self.x:
                last_pos = index
        return [first_pos, last_pos]

if __name__ == '__main__':
    print(Solution([1,2,3,4,1,2,7,2,8,9], x=2).find_positions()) # [1,7]
    print(Solution([], x=2).find_positions()) # [-1, -1]
    print(Solution([1,2,3], x=2).find_positions()) # [1,1]