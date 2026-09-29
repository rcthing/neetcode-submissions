class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = defaultdict(list)

        for word in strs:
            table = [0] * 26
            for ch in word:
                table[ord(ch) - ord('a')] += 1

            dct[tuple(table)].append(word)


        return list(dct.values())
                
