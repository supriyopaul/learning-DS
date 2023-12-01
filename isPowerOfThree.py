class Solution:
    
    def isPowerOfThree(self, n: int) -> bool:

        def multiply3(num):
            if num == n: return True
            elif num > n: return False
            else: return multiply3(num*3)
        
        return multiply3(1)

if __name__ == '__main__':
    solution = Solution()
    print(solution.isPowerOfThree(27)) # True
    print(solution.isPowerOfThree(0)) # False
    print(solution.isPowerOfThree(-1)) # False
    print(solution.isPowerOfThree(1)) # True
    print(solution.isPowerOfThree(45)) # False