class Solution:
    def bitsToInt(self, n:int) -> int:
        bit_string = reversed(str(n))
        result_value = 0
        for index, bit in enumerate(bit_string):
            result_value += int(bit) * 2**index # (0*2^0) + (1*2^1)
        return result_value

    def reverseBits(self, n: int) -> int:
        
        reversed_bits = str(int(n))[::-1]
        if not len(reversed_bits) == 32:
            reversed_bits = reversed_bits + '0'*(32-len(reversed_bits))

        return self.bitsToInt(reversed_bits)

if __name__ == '__main__':
    sol = Solution()
    print(sol.reverseBits(10100101000001111010011100)) # 43261596 -> 964176192
    print(sol.reverseBits(11111111111111111111111111111101)) # 4294967293 -> 3221225471