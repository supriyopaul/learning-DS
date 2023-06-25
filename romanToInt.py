class Solution:

    ROMAN_NUMERALS = ("I", "V", "X", "L", "C", "D", "M")
    VALUES = (1, 5, 10, 50, 100, 500, 1000)
    VALUE_MAP = {k:v for k, v in zip(ROMAN_NUMERALS, VALUES)}

    def romanToInt(self, s: str) -> int:
        """
        "III"
        "LVIII"
        "MCMXCIV"
        """
        result = 0
        if len(s) > 15: return 0
        for index in range(len(s)):
            roman_numeral = self.VALUE_MAP[s[index]]
            try:
                next_roman_numeral = self.VALUE_MAP[s[index+1]]
            except IndexError:
                next_roman_numeral = None
            if next_roman_numeral and (roman_numeral <= next_roman_numeral):
                result -= roman_numeral
            else:
                result += roman_numeral
        return result

if __name__ == "__main__":
    print(Solution().romanToInt("MCMXCIIIV"))