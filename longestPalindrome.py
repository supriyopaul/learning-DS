class Solution:

    def longestPalindrome(self, s: str) -> str:
        str_len = len(s)
        self.longest_palindrome = s[0]

        def check_palindrome(s):
            #print(f"checking for:{s}")
            if not s[0] == s[-1]: return

            if s == s[::-1] and len(s) > len(self.longest_palindrome):
                self.longest_palindrome = s

        def expand_around(center):
            
            boundary = min(center, str_len-center)
            #print(f"boundary:{boundary}, center:{s[center]}")
            for b in range(0, boundary+1):
                left_boundary = center-b
                right_boundary = center+b+1
                # odd length palindrome
                
                check_palindrome(s[left_boundary:right_boundary])
                # even length palindrome
                if right_boundary < str_len:
                    check_palindrome(s[left_boundary:right_boundary+1])
            
        for index, char in enumerate(s):
            if not len(self.longest_palindrome) > str_len - index: 
                expand_around(center=index)
        
        return self.longest_palindrome




if __name__ == '__main__':
    solution = Solution()
    print(solution.longestPalindrome("babad")) #bab
    print(solution.longestPalindrome("cbbd")) #bb