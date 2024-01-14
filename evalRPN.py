from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "*", "/"}
        stack = []
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                a = stack.pop(-1)
                b = stack.pop(-1)
                if token == "+":
                    evaluation =  a + b
                    stack.append(evaluation)
                elif token == "-":
                    evaluation = b - a
                    stack.append(evaluation)
                elif token == "*":
                    evaluation = a * b
                    stack.append(evaluation)
                else:
                    evaluation = int(b / a)
                    stack.append(evaluation)
        return stack.pop(-1)



if __name__ == "__main__":
    obj = Solution()
    print(obj.evalRPN(tokens = ["2","1","+","3","*"])) # 9
    print(obj.evalRPN(tokens = ["4","13","5","/","+"])) # 6
    print(obj.evalRPN(tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"])) # 22