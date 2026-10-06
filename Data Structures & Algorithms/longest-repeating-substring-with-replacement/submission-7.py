class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        chardict = {}
        maxlen = 0
        for r in range(len(s)):
            chardict[s[r]] = chardict.get(s[r], 0) + 1
            count = r - l + 1 - max(chardict.values())

            while count > k:
                chardict[s[l]] -= 1
                l += 1
                count = r - l + 1 - max(chardict.values())
            
            maxlen = max(maxlen, r - l + 1)
        return maxlen