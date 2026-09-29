class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        dct = defaultdict(list)

        for word in strs:
            table = [0] * 26
            for ch in word:
                table[ord(ch) - ord('a')] += 1

            dct[tuple(table)].append(word)

        for k in dct:
            res.append(dct[k])
        return res
                
