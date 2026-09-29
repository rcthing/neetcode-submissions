class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        res = []
        for i in range(len(nums)):
            if target - nums[i] in dictionary:
                res.append(dictionary[target - nums[i]])
                res.append(i)
                return res
            dictionary[nums[i]] = i