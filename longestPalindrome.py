class Solution:

    def longestPalindrome(self, s: str) -> str:
        l = 0
        r = len(s)
        counter = 0
        while l < r:
            #import pdb; pdb.set_trace()
            print(s[l:r] + '==' + s[l:r][::-1])
            if s[l:r] == s[l:r][::-1]:
                return s[l:r]
            elif counter%2 == 0:
                l += 1
                counter += 1
            else: r -= 1
        



if __name__ == '__main__':
    solution = Solution()
    print(solution.longestPalindrome("babad")) #bab
    print(solution.longestPalindrome("cbbd")) #bb