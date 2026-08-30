class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            l = len(s)
            res = res + str(l) + "#" + s
        
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j=i
            while s[j] != "#":
                j += 1
            
            ln = int(s[i:j])

            start = j + 1
            end = j + 1 + ln

            res.append(s[start:end])

            i = end
        return res

