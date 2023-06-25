import re
from ast import literal_eval

class Solution:
    def myAtoi(self, s: str) -> int:
        digits = ""
        min_value = -2147483648
        max_value = 2147483647
        for c in s:
            if c.isspace() and not digits : continue
            elif (c == '+' or c == '-') and (not digits): digits += c
            elif (c == '+' or c == '-') and digits: return 0
            elif c.isnumeric(): digits += c
            elif not c.isnumeric() and digits: break
            else: return 0
        print(digits)
        result = literal_eval(digits)
        if result < min_value: return min_value
        elif result > max_value: return max_value
        else: return result

if __name__ == '__main__':
    print(Solution().myAtoi("42"))
    print(Solution().myAtoi("   -42 with words"))
    print(Solution().myAtoi("words and 987"))
    print(Solution().myAtoi("+-42"))
    print(Solution().myAtoi("-+12"))