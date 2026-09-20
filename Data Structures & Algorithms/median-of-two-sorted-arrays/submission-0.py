class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        if len(B) < len(A):
            A, B = B, A # ensure A is the smaller array (if theres one)

        total = len(A) + len(B)
        l, r = 0 , len(A)-1 
        half = total//2 #half point of the 'merged' array

        # B = [2,4,5,6,7,8,9]
        # A = [1,3,4,5]
        while True:
            i = (r+l) // 2
            j = half - i -2 # zero indexed 

            Aleft = A[i] if i >= 0 else float('-infinity')
            Aright = A[i+1] if i+1 < len(A) else float('infinity')
            Bleft = B[j] if j >= 0 else float('-infinity')
            Bright = B[j+1] if j+1 < len(B) else float('infinity')

            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if (total % 2 == 1):
                    return min(Aright, Bright)
                else:
                    return (max(Aleft,Bleft) + min(Aright, Bright)) /2
            elif Aleft > Bright:
                r = i-1
            elif Bleft > Aright:
                l = i + 1



