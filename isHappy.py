class Solution:
    def isHappy(self, n: int) -> bool:
        sum_of_squares = n
        _sums = set()
        def _get_sum_of_squares(num):
            if num < 10: return num*num
            else: return _get_sum_of_squares(num%10) + _get_sum_of_squares(num//10)
        
        while sum_of_squares != 1:
            print(sum_of_squares)
            sum_of_squares = _get_sum_of_squares(sum_of_squares)
            if sum_of_squares not in _sums:
                _sums.add(sum_of_squares)
            else: return False

        
        return True

if __name__ == "__main__":
    print(Solution().isHappy(19))
    print(Solution().isHappy(2))