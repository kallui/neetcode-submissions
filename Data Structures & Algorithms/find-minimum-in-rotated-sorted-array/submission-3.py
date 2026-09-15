class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1

        while l < r:
            mid = (l+r) // 2 # floor
            #Input: nums = [3,4,5,6,1,2]
            # Input: nums = [4,5,0,1,2,3]
            # Input: nums = [4,5,6,7]
            # nums=[2,1]
            if nums[mid] < nums[r]:
                # Same segment, that means r has the smaller segment.
                r = mid
            else:
                # Mid is on the left segment, that means mid cannot be answer, so can safely do mid+1
                l = mid +1

        return nums[l]