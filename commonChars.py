from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        word_occurences = list()
        result = list()
        
        for word in words:
            word_dict = dict()
            for letter in word:
                if letter not in word_dict: word_dict[letter] = 1
                else: word_dict[letter] += 1
            word_occurences.append(word_dict)
        common_occurences = word_occurences[0]
        
        for i in range(1, len(word_occurences)):
            word_dict = word_occurences[i]
            for letter, occurence in common_occurences.items():
                if letter not in word_dict or common_occurences[letter] == 0:
                    common_occurences[letter] =  0
                else:
                    common_occurences[letter] = min(occurence, word_dict[letter])
        
        for letter, occurence in common_occurences.items():
            if not occurence == 0:
                result.extend([letter]*occurence)
        return result




if __name__ == "__main__":
    print(Solution().commonChars(["bella","label","roller"])) #Output: ["e","l","l"]
    print(Solution().commonChars(["cool","lock","cook"])) #Output: ["c","o"]
