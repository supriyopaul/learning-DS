from typing import List

class Solution:
    
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1]
        if rowIndex == 1: return [1,1]

        triangle_dict = dict()
        for index in range(rowIndex+1):
            if index == 0:
                triangle_dict[index] = [1]
                continue
            if index == 1:
                triangle_dict[index] = [1,1]
                continue

            previous_index = index - 1
            previous_row = triangle_dict[previous_index]
            row = [1] + [None]*(index-1) + [1]

            for i, element in enumerate(row):
                if element == 1: continue
                else:
                    element = previous_row[i] + previous_row[i-1]
                    row[i] = element
            triangle_dict[index] = row
        print(triangle_dict)
        return triangle_dict[rowIndex]


if __name__ == "__main__":
    print(Solution().getRow(0))
    print(Solution().getRow(1))
    print(Solution().getRow(3))
    print(Solution().getRow(4))