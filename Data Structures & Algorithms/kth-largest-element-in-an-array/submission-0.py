import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for x in nums:
            heapq.heappush(heap, x) # min heap

            if len(heap) > k:
                heapq.heappop(heap) # pop to ensure heap[0] the smallest element AKA (kth largest element)
        
        return heap[0]