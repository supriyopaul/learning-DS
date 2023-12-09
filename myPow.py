from functools import lru_cache

class Solution:
    
    @lru_cache
    def _r_myPow(self, x: float, n: int) -> float:
        if n==0: return 1.0
        if n==1: return x
        if n%2 == 0:
            return self._r_myPow(x, n/2) * self._r_myPow(x, n/2)
        else:
            return self._r_myPow(x, (n-1)/2) * self._r_myPow(x, (n-1)/2) * x
        
    def myPow(self, x: float, n: int) -> float:
        _pow = self._r_myPow(x, abs(n))
        if n < 0: return 1/_pow
        return _pow

if __name__ == '__main__':
    print(Solution().myPow(x=2.00000, n=10)) # 1024.00000
    print(Solution().myPow(x=2.10000, n=3)) # 9.26100
    print(Solution().myPow(x=2.00000, n=-2)) # 0.25
    print(Solution().myPow(x=0.00001, n=2147483647)) # 0.25