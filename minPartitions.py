class Solution:
    def minPartitions(self, n: str) -> int:
        _max = 0
        for char in n:
            _max = max(_max, int(char))
        return _max


if __name__ == "__main__":
    print(Solution().minPartitions("32"))
    print(Solution().minPartitions("82734"))
    print(Solution().minPartitions("27346209830709182346"))