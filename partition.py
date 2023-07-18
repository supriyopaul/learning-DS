from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        str_len = len(s)

        def is_palindrome(s):
            if s == s[::-1]: return True
            else: return False

        result = []
        window =  1
        for i in range(len(s)):
            for window in range(i):
                slice = s[i:window+1]
                print(slice)

            
            

if __name__ == '__main__':
    s = "aab"
    print(Solution().partition(s)) #Output: [["a","a","b"],["aa","b"]]
    s = "a"
    print(Solution().partition(s)) #Output: [["a"]]