class Solution(object):
    def topKFrequent(self, nums, k):
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        n = len(nums)
        buckets = [[] for _ in range(n + 1)]
        for num, freq in freq_map.items():
            buckets[freq].append(num)

        result = []
        for freq in range(n, -1, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result

        return result