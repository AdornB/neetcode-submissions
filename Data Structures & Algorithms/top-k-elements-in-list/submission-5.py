class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
        sortedNums = sorted(counts, key=counts.get, reverse=True)
        results = []
        for i in range(k):
            results.append(sortedNums[i])
        return results