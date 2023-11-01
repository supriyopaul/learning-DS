from typing import List

class Solution:
    def get_binary(self, n):
        binary = ""
        while n > 1:
            binary = binary + str(n%2)
            n = n//2
        return (binary + str(n))[::-1]


    def countBits(self, n: int) -> List[int]:
        bits_dict = dict()
        for i in range(n+1):
            if i == 0: bits_dict[i] = 0
            if i == 0: bits_dict[i] = 1
            bits_dict[i] = self.get_binary(i)
        
        output = []
        for number, binary in bits_dict.items():
            _sum = 0
            for char in binary:
                _sum += int(char)
            output.append(_sum)
        return output

if __name__ == "__main__":
    print(Solution().countBits(2))
    print(Solution().countBits(5))