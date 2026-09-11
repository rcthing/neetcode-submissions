class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(cur_sum, path):
            if cur_sum == target:
                ans.append(path[:])
                return
            elif cur_sum > target:
                return
            else:
                for n in nums:
                    if len(path) == 0:
                        dfs(cur_sum + n, path + [n])
                    elif n >= path[len(path) - 1]:
                        dfs(cur_sum + n, path + [n])
                    else:
                        continue

        dfs(0, [])
        return ans