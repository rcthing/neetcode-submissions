class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charD = defaultdict(int)
        l = 0
        longest = 0

        for r in range(len(s)):
            charD[s[r]] += 1

            check = r - l + 1 - max(charD.values())
            if check > k:
                longest = max(longest, r - l)
                while check > k:
                    charD[s[l]] -= 1
                    l += 1
                    check = r - l + 1 - max(charD.values())
            else:
                longest = max(longest, r - l + 1)
        return longest

