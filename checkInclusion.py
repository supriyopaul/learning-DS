from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        start, end  = 0, len(s1)
        s1_dict = Counter(s1)
        while end <= len(s2):
            if Counter(s2[start:end]) == s1_dict:
                return True
            start += 1
            end += 1
        return False


    
if __name__ == '__main__':
    sol = Solution()
    
    s1 = "ab"
    s2 = "eidbaooo"
    print(sol.checkInclusion(s1, s2)) # true

    s1 = "ab"
    s2 = "eidboaoo"
    print(sol.checkInclusion(s1, s2)) # false

    s1 = "adc"
    s2 = "dcda"
    print(sol.checkInclusion(s1, s2)) # false