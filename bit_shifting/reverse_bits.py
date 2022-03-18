class SolutionA:
    def reverseBits(self, n: int, bits) -> int:
        s = ""
        for i in range(bits):
            if n & 1 << i: # using bitwise AND determines if the bit at that position is 1
                s += "1"
            else:
                s += "0"
        return int(s, 2)

class SolutionB:
    def reverseBits(self, n: int, bits) -> int:
        res = 0
        for i in range(bits):
            res <<= 1
            # instead of shifting the 1 bit in 1, shift the whole number and always
            # check the less significant bit
            res = res | (n & 1)
            n >>= 1
        return res

n = 43261596
n = 8

print(SolutionA().reverseBits(n, 4))
print(SolutionB().reverseBits(n, 4))
        