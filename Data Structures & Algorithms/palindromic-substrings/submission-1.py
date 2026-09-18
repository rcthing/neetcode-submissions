class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for k in range(len(s)):
            i = j = k

            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
                res += 1
            i = k
            if i + 1 < len(s) and s[i] == s[i+1]:
                j = i + 1
                while i >= 0 and j < len(s) and s[i] == s[j]:
                    res += 1
                    i -= 1
                    j += 1

        return res