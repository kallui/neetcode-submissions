import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        res = []

        l = 0

        for r in range(len(nums)):
            heapq.heappush(heap, (-nums[r], r))
            
            if r < k-1:
                continue
            
            l = r - k + 1
            # remove outdated index
            while heap and heap[0][1] < l:
                heapq.heappop(heap)

            res.append(-heap[0][0])
            r += 1

        return res

