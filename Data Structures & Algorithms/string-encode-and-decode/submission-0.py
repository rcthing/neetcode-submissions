class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i<len(s):
            j = i
            while s[j] != "#":
                j += 1
            nr = int(s[i:j]) # merge pana la j-1
            res.append(s[j+1:j+nr+1])
            i = j + nr + 1
        return res
