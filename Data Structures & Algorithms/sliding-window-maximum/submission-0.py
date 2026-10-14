import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        res = []

        l, r = 0, k-1

        while r < len(nums):
            #init iter
            if r == k-1:
                for i, x in enumerate(nums[l:r+1]):
                    heapq.heappush(heap, (-x, i)) # (-value, index); use -value bcs its a minheap and we want the max
            # after initial window
            else:
                heapq.heappush(heap, (-nums[r], r))
            
            # remove outdated index
            while heap and heap[0][1] < l:
                heapq.heappop(heap)

            res.append(-heap[0][0])
            l += 1
            r += 1
        return res

