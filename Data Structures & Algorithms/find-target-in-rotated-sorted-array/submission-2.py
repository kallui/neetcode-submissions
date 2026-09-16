class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n-1

        while l <= r:
            mid = (l+r) // 2 # floor

            # nums = [3,4,5,6,1,2], target = 1
            # nums = [,6,1,2,3,4,5], target = 1
            # nums=[4,5,6,7,0,1,2] target=0
            # nums=[3,5,6,0,1,2] target=4
            if nums[mid] == target:
                return mid
            elif nums[mid] > nums[r]: # mid is on left segment
                if nums[l] <= target < nums[mid]:
                    r = mid -1
                else:
                    l = mid+1
            else: # mid is on right segment
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else: 
                    r = mid -1

        return -1