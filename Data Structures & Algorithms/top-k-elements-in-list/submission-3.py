class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for n in nums:
            count[n] += 1

        freq = [[] for _ in range(len(nums) + 1)]
        for el, c in count.items():
            freq[c].append(el)
        
        ans = []
        for i in range(len(nums), 0, -1):
            for el in freq[i]:
                ans.append(el)
                k -= 1
                if k == 0:
                    return ans