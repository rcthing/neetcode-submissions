class Solution:
    def numDecodings(self, s: str) -> int:
        next1 = next2 = 1
        for i in range(len(s) - 1, -1, -1):
            curent = 0
            if s[i] != "0":
                curent += next1

            if i < len(s) - 1 and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456"):
                curent += next2

            next2 = next1
            next1 = curent

        return curent
