class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()

        maxl = 0
        l,r = 0, 0

        while r < len(s):

            if s[r] not in char_set:
                char_set.add(s[r])
                r += 1
            else:
                while s[r] in char_set:
                    char_set.remove(s[l])
                    l += 1

            if r - l > maxl:
                maxl = r - l
        return maxl
