class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        chardict = {}
        maxlen = 0
        maxf = 0
        for r in range(len(s)):
            chardict[s[r]] = chardict.get(s[r], 0) + 1
            maxf = max(maxf, chardict[s[r]])

            while r - l + 1 - maxf > k:
                chardict[s[l]] -= 1
                l += 1
            
            maxlen = max(maxlen, r - l + 1)
        return maxlen