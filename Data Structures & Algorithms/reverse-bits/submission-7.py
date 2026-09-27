class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        i = 0
        while n and i < 32:
            bit = n % 2
            n = n >> 1
            if bit:
                res = res | (bit << (31 - i))
            i += 1
        return res