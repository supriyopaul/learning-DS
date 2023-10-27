class Solution:
    def __init__(self) -> None:
        self.memo = {}

    def uniquePaths(self, m: int, n: int) -> int:
        if (m, n) in self.memo: return self.memo[(m, n)]

        if m == 1 and n == 1: return 1
        elif m == 1 or n == 1: return 1

        self.memo[(m, n)] = (self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1))
        return self.memo[(m, n)]


if __name__ == "__main__":
    print(Solution().uniquePaths(m=3, n=7))
    print(Solution().uniquePaths(m=3, n=2))
