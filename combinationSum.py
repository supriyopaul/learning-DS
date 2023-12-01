from typing import List
from pprint import pprint


class Solution:
    '''
    2: 2
    4: 22
    6: 222, 33, 6
    3: 3
    7: 7
    '''

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sum_dict = {}
        for candidate in candidates:
            for i in range(1, int((target+1)/2)):
                combination = [candidate]*i
                combination_sum = sum(combination)
                if combination_sum > target:
                    break
                if combination_sum in sum_dict:
                    sum_dict[combination_sum].append(combination)
                else:
                    sum_dict[combination_sum] = [combination]

        pprint(sum_dict)
        result  = set()

        for _sum in sum_dict:
            if _sum == target:
                result.update(tuple(sorted(sublist)) for sublist in sum_dict[_sum])
            if (target - _sum) in sum_dict and (target - _sum) > _sum:
                l1 = sum_dict[target - _sum]
                l2 = sum_dict[_sum]
                combined = [tuple(sorted(x+y)) for x in l1 for y in l2]
                result.update(combined)
        
        return [list(r) for r in result]



if __name__ == '__main__':
    solution = Solution()
    print(solution.combinationSum(candidates=[2,3,6,7], target=7)) # [[2,2,3],[7]]
    print(solution.combinationSum(candidates=[2,3,5], target=8)) # [[2,2,2,2],[2,3,3],[3,5]]
    print(solution.combinationSum(candidates=[3,5,7], target=9)) # [[3,3,3]]