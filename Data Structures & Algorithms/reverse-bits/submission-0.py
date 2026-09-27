class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        nr = 2147483648
        while n:
            if n % 2:
                res +=  nr
                # n = n & (n - 1)

            nr /= 2
            n = n >> 1
        return int(res)