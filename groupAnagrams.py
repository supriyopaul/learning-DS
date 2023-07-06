from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()
        for word in strs:
            letters = tuple(sorted([i for i in word]))
            if letters not in anagrams:
                anagrams[letters] = [word]
            else:
                anagrams[letters].append(word)


        return [a for a in anagrams.values()]


if __name__ == '__main__':
    print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    print(Solution().groupAnagrams([""]))
    print(Solution().groupAnagrams(["a"]))