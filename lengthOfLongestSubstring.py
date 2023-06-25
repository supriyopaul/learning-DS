class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        max_length = 1
        char_set = set()
        while end < len(s):
            if s[end] not in char_set:
                char_set.add(s[end])
                end += 1
            else:
                char_set.remove(s[start])
                start += 1
            max_length = max(max_length, (end-start))
            #print(char_set)
        return max_length


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLongestSubstring("abcabcbb")) #3
    print(solution.lengthOfLongestSubstring("bbbbb")) #1
    print(solution.lengthOfLongestSubstring("pwwkew")) #3