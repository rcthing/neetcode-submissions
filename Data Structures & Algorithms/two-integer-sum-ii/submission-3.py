class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans = []
        l = 0
        r = len(numbers) - 1
        s = 0

        while l < r:
            if (s + numbers[l] + numbers[r]) > target:
                r -= 1
            elif (s + numbers[l] + numbers[r]) < target:
                l += 1
            else :
                ans.append(l+1)
                ans.append(r+1)
                return ans
        