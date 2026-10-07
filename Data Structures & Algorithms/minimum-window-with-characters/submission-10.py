class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        need = defaultdict(int)
        have = defaultdict(int)

        lmin, rmin = 0, len(s)

        for c in t:
            need[c] += 1

        h, n = 0, len(need)

        l = 0
        found = 0
        for r in range(len(s)):
            if s[r] in need:
                have[s[r]] += 1
                if have[s[r]] == need[s[r]]:
                    h += 1
            while n == h:
                found = 1
                if rmin - lmin > r - l:
                    lmin = l
                    rmin = r
                if s[l] in have.keys():
                    have[s[l]] -= 1
                    if have[s[l]] < need[s[l]]:
                        h -= 1
                l += 1
        return s[lmin : rmin + 1] if found == 1 else ""

        