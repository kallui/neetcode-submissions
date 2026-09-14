class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        u, d = 0, len(matrix)-1
        l, r = 0, len(matrix[0])-1

        row = -1
        while u <= d:
            midY = (u+d)//2
            
            if matrix[midY][0] <= target and target <= matrix[midY][-1]:
                row = midY
                break;
            elif matrix[midY][-1] < target:
                u = midY+1
            elif matrix[midY][0] > target:
                d = midY-1
        
        print(u)
        while l <=r:
            midX = (l+r)//2
            
            if matrix[row][midX] == target:
                return True
            elif matrix[row][midX] < target:
                l = midX+1
            elif matrix[row][midX] > target:
                r = midX-1
        return False

        
