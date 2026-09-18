class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxi = 0
        imax = 0
        jmax = 0
        for k in range(len(s)):
            j = i = k
            tmax = 0
            if k < len(s) - 1 and s[i] == s[i+1]:
                j += 1
                while i >= 0 and j < len(s) and s[i] == s[j]:
                    tmax += 2
                    i -= 1
                    j += 1

                if tmax > maxi:
                    maxi = tmax
                    imax = i + 1
                    jmax = j - 1

                i = j = k
                tmax = 0

            while i >= 0 and j < len(s) and s[i] == s[j]:
                tmax += 2
                i -= 1
                j += 1
            tmax -= 1
            if tmax > maxi:
                maxi = tmax
                imax = i + 1
                jmax = j - 1
        
        return s[imax:jmax+1]
