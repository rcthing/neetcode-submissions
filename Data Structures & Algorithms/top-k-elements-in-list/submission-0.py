class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        length =  len(nums)
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = count.get(n, 0) + 1

        for n, c in count.items():
            freq[c].append(n)

        res = []

        for i in range(len(freq) - 1, 0, -1):
            for val in freq[i]:
                res.append(val)
                k -= 1
                if k == 0:
                    return res
