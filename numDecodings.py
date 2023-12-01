class Solution:
    def numDecodings(self, s: str) -> int:
        '''

        '''
        if s[0] == '0':
            return 0

        dp = {0: 1, 1:1}
        for i in range(2, len(s)+1):
            
            if dp[i] != '0':
                dp[i] +=  dp[i-1]
            if 10 >= int(s[i:i+2]) <= 26:
                dp[i] += dp[i-2]

        return dp[len(s)]



if __name__ == '__main__':
    solution = Solution()
    print(solution.numDecodings("12")) # 2
    print(solution.numDecodings("226")) # 3
    print(solution.numDecodings("06")) # 0
    print(solution.numDecodings("226710")) # 0