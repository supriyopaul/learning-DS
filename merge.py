from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        length = len(intervals)
        if length == 1: return intervals
        sorted_intervals = []
        mergerd_intervals = []
        for interval in intervals:
            sorted_intervals.append((interval[0], 'b'))
            sorted_intervals.append((interval[1], 'e'))
        
        sorted_intervals = sorted(sorted_intervals)
        index = 0
        stack = []

        while index < len(sorted_intervals):
            if sorted_intervals[index][1] == 'b':
                stack.append(sorted_intervals[index])
            if sorted_intervals[index][1] == 'e':
                start = stack.pop(-1)[0]
                end = sorted_intervals[index][0]
                if not stack: mergerd_intervals.append([start, end])
            index += 1

        return mergerd_intervals


if __name__ == '__main__':
    print(Solution().merge(intervals = [[1,3],[2,6],[8,10],[15,18]])) # [[1,6],[8,10],[15,18]]
    print(Solution().merge([[1,4],[4,5]])) # [[1,5]]
    print(Solution().merge([[1,4],[2,3]])) # [[1,4]]