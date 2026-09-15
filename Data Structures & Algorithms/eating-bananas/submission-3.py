from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # upper bound for k = max(piles)
        l, r = 1, max(piles)

        minimumK = r

        while l <= r:
            mid = (l+r)//2

            hours = 0
            for i, v in enumerate(piles):
                hours += ceil(v/mid)
            if hours <= h:
                minimumK = min(minimumK, mid)
                r = mid - 1
            else:
                l = mid +1

        return minimumK

