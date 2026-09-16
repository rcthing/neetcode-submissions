class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atlantic = set()
        pacific = set()

        def dfs(i,j, ocean, height):
            if (i<0 or i>=len(heights) or j<0 or j>=len(heights[0]) 
            or(i,j) in ocean or heights[i][j] < height):
                return

            ocean.add((i,j))
            dfs(i+1, j, ocean, heights[i][j])
            dfs(i-1, j, ocean, heights[i][j])
            dfs(i, j+1, ocean, heights[i][j])
            dfs(i, j-1, ocean, heights[i][j])

        for j in range(len(heights[0])):
            dfs(0, j, pacific, heights[0][j])
            dfs(len(heights)-1, j, atlantic, heights[len(heights)-1][j])

        for i in range(len(heights)):
            dfs(i, 0, pacific, heights[i][0])
            dfs(i, len(heights[0])-1, atlantic, heights[i][len(heights[0])-1])

        intersection = atlantic.intersection(pacific)
        return [[i,j] for (i,j) in intersection]