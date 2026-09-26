class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        res = 0

        def dfs(r,c):
            if (r >= len(grid) or c >= len(grid[r]) or r < 0 or c < 0
                or (r,c) in seen
                or grid[r][c] == "0"):
                return
            
            seen.add((r,c))

            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)

        for r, i in enumerate(grid):
            for c, j in enumerate(grid[r]):
                if j == "1" and (r,c) not in seen:
                    # check all ways
                    res +=1
                    dfs(r,c)
        return res