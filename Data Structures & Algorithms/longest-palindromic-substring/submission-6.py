class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxi = imax = jmax = 0
        for k in range(len(s)):
            j = i = k

            if k < len(s) - 1 and s[i] == s[i+1]:
                j += 1
                while i >= 0 and j < len(s) and s[i] == s[j]:
                    i -= 1
                    j += 1

                if j - i - 1 > maxi:
                    maxi = j - i - 1
                    imax = i + 1
                    jmax = j - 1

                i = j = k

            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1

            if j - i - 1 > maxi:
                maxi = j - i - 1
                imax = i + 1
                jmax = j - 1
        
        return s[imax:jmax+1]
