class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        res = []
        for n in nums:
            count[n] = count.get(n, 0) + 1

        for el, frecv in count.items():
            freq[frecv].append(el)

        i = len(nums)
        while k:
            if freq[i]:
                for el in freq[i]:
                    res.append(el)
                    k -= 1

            i -= 1
        return res

        
