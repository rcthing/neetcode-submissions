class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int) #initializeaza automat cu 0
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] += 1

        for n, count in count.items():
            freq[count].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for val in freq[i]:
                res.append(val)
                k -= 1
                if k == 0:
                    return res
