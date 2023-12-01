class Solution:

    def letterCombinations(self, s: str) -> str:
        '''
        a, b , c

        '''

        key_map = {
            "": [],
            "2": ["a","b","c"],
            "3": ["d","e","f"],
            "4": ["g","h","i"],
            "5": ["j","k","l"],
            "6": ["m","n","o"],
            "7": ["p","q","r", "s"],
            "8": ["t","u","v"],
            "9": ["w","x","y", "z"]
        }
        index = 1
        while index < len(s):
            
            previous_string = s[0:index]
            current_char = s[index]
            key_map[previous_string+current_char] = []

            for string in key_map[previous_string]:
                for char in key_map[current_char]:
                    key_map[previous_string+current_char].append(string+char)
               
            index += 1
        return key_map[s]

if __name__ == '__main__':
    solution = Solution()
    print(solution.letterCombinations("")) #
    print(solution.letterCombinations("2")) #["a","b","c"]
    print(solution.letterCombinations("23")) #["ad","ae","af","bd","be","bf","cd","ce","cf"]