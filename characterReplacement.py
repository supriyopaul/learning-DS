
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # start with start and end at 0
        start, end = 0, 0
        max_window = 0
        max_frequency = 0
        count = {}

        # until end reaches the 2nd last character in s
        while end < len(s):
            # If window start to end is a valid substring
            if s[end] in count:
                count[s[end]] += 1
            else:
                count[s[end]] = 1

            max_frequency = max(max_frequency, max(count.values()))
            
            if max_frequency + k >= (end+1)-start:
                max_window += 1
            else:
                count[s[start]] -= 1
                start = start + 1
                
            end = end + 1

        return max_window
    
if __name__ == '__main__':
    sol = Solution()
    
    s = "ABAB"
    k = 2
    print(sol.characterReplacement(s, k)) # 4

    s = "AABABBA"
    k = 1
    print(sol.characterReplacement(s, k)) # 4