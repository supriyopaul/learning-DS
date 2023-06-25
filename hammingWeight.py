class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        for bit in str(n):
            if bit == "1": result += 1
            else: continue
        return result


if __name__ == '__main__':
    print(Solution().hammingWeight(1011))