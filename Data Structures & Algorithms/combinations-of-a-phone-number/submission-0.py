class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if not digits: return res
        
        digitsMap = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", 
                        "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def dfs(i,subset):
            if i >= len(digits):
                res.append(subset)
                return
            
            for c in digitsMap[digits[i]]:
                subset += c

                dfs(i+1, subset)
                subset = subset[:-1]
        dfs(0, "")
        return res

