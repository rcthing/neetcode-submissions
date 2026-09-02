class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": 
            return ""

        countT = {}
        for char in t:
            countT[char] = countT.get(char, 0) + 1
        need = len(countT)
        have = 0
        l = 0
        lf = 0
        rf = len(s) + 1
        min_len = len(s) + 1

        for r in range(len(s)):
            if s[r] in countT:
                countT[s[r]] -= 1
                if countT[s[r]] == 0:
                    have += 1
            
            while have == need:
                if r-l+1 < min_len:
                    lf, rf = l, r
                    min_len = r-l+1
                
                if s[l] in countT:
                    countT[s[l]] += 1
                    if countT[s[l]] > 0:
                        have -= 1
                l += 1

        return s[lf:rf+1] if min_len != len(s) + 1 else ""



