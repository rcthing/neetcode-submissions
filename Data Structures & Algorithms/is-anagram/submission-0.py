class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = {}
        for char in s:
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1
        
        for char in t:
            if char in counter:
                counter[char] -= 1
            else:
                return False

        for val in counter.values():
            if val != 0:
                return False
        return True