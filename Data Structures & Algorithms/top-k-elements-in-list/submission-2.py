import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}

        for x in nums:
            if x not in count:
                count[x] = 1
            else:
                count[x] += 1
        
        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))

            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for freq, num in heap:
            res.append(num)

        return res
            