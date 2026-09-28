class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while b:
            xor = a ^ b
            carry = (a & b) << 1

            a = xor 
            b = carry
            a &= mask
            b &= mask
        if a < 0x7FFFFFFF:
            return a
        return ~(a ^ mask)