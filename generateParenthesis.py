from typing import List
from itertools import combinations, permutations


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        input_str = '()'*n
        result = set()
        _combinations = set(permutations(input_str))
        print("created combinations")
        for combination in _combinations:
            if not len(combination) == n*2: continue
            paranthesis_str = ""
            for p in combination: paranthesis_str += p
            #print(paranthesis_str)
            if self.paranthesis_valid(paranthesis_str): result.add(paranthesis_str)
        return list(result)

    def paranthesis_valid(self, p: str) -> bool:
        stack = []
        for bracket in p:
            if bracket == "(":
                stack.append(bracket)
            elif bracket == ")":
                if not stack or stack.pop() != "(": return False
            
        if stack: return False
        return True


if __name__ == '__main__':
    #print(Solution().paranthesis_valid("(()())"))
    #print(Solution().paranthesis_valid("()())"))
    #print(Solution().generateParenthesis(3)) #Output: ["((()))","(()())","(())()","()(())","()()()"]
    print(Solution().generateParenthesis(6)) #Output: ["()"]
    