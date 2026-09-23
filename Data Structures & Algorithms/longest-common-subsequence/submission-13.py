class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text2) < len(text1):
            text1, text2 = text2, text1
        before_row = [0] * (len(text1) + 1)
        curent_row = [0] * (len(text1) + 1)

        for i in range(len(text2) -1, -1, -1):
            for j in range(len(text1) -1, -1, -1):
                if text2[i] == text1[j]:
                    curent_row[j] = before_row[j+1] + 1
                else:
                    curent_row[j] = max(before_row[j], curent_row[j+1])
            before_row, curent_row = curent_row, before_row

        return before_row[0]