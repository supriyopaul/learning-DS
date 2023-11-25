from typing import List
from itertools import combinations, permutations


class Solution:

    def insert_parnthesis(self, original_parenthesis ,index):
        start = original_parenthesis[:index]
        end = original_parenthesis[index:]
        return start + "()" + end

    def generateParenthesis(self, n: int) -> List[str]:
        '''
        ()
        (()) ()()
        ()(()) (())() ((())) (()()) ()()()
        '''
        p_dict = {
            1: ["()"],
            
        }
        if n == 1: return p_dict[n]
        for i in range(2, n+1):
            ith_parenthesis_set = set()
            previous_parenthesis_list = p_dict[i-1]
            for p in previous_parenthesis_list:
                for index in range(0, len(p)):
                    new_p = self.insert_parnthesis(original_parenthesis=p, index=index)
                    ith_parenthesis_set.add(new_p)
            p_dict[i] = list(ith_parenthesis_set)
        return p_dict[n]


if __name__ == '__main__':
    print(Solution().generateParenthesis(1))
    print(Solution().generateParenthesis(2))
    print(Solution().generateParenthesis(3))
    print(Solution().generateParenthesis(10))
    