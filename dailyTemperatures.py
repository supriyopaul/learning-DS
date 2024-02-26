from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = list()
        for index, value in enumerate(temperatures):
            if not stack or value < stack[-1][1]:
                stack.append((index, value))
                continue
            while stack and value > stack[-1][1]:
                last_element = stack.pop(-1)
                result[last_element[0]] = index - last_element[0]
            stack.append((index, value))

        return result



if __name__ == "__main__":
    obj = Solution()
    print(obj.dailyTemperatures([73,74,75,71,69,72,76,73]))  # [1,1,4,2,1,1,0,0]
    print(obj.dailyTemperatures([30,40,50,60]))  # [1,1,1,0]
    print(obj.dailyTemperatures([30,60,90]))  # [1,1,0]