from collections import deque

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:

        n = len(grid)

        dist = [[-1] * n for _ in range(n)]

        q = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i, j))

        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        while q:
            x, y = q.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

        def canReach(limit):

            if dist[0][0] < limit or dist[n-1][n-1] < limit:
                return False

            vis = [[False] * n for _ in range(n)]
            bfs = deque([(0, 0)])
            vis[0][0] = True

            while bfs:

                x, y = bfs.popleft()

                if x == n - 1 and y == n - 1:
                    return True

                for dx, dy in directions:

                    nx, ny = x + dx, y + dy

                    if 0 <= nx < n and 0 <= ny < n:
                        if not vis[nx][ny] and dist[nx][ny] >= limit:
                            vis[nx][ny] = True
                            bfs.append((nx, ny))

            return False

        left = 0
        right = 2 * n
        ans = 0

        while left <= right:

            mid = (left + right) // 2

            if canReach(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
    

#Time Complexity: O(n^2 * log(n))
#Space Complexity: O(n^2)
'''
here's a breakdown of the code:
1. Initialization: The code initializes a distance matrix `dist` to store the minimum distance from each cell to 
    the nearest cell containing a 1. It also initializes a queue `q` to perform a breadth-first search (BFS) to 
    fill in the `dist` matrix.

2. BFS for Distance Calculation: The code performs a BFS starting from all cells containing a 1 to calculate the 
    minimum distance to the nearest 1 for each cell in the grid. The distances are stored in the `dist` matrix.

3. Binary Search for Maximum Safeness Factor: The code uses binary search to find the maximum safeness factor. 
    It defines a helper function `canReach(limit)` that checks if there is a path from the top-left corner to the 
    bottom-right corner of the grid such that all cells in the path have a distance greater than or equal to `limit`.

4. Path Checking: The `canReach` function performs a BFS to check if a valid path exists for the given `limit`. 
    It returns `True` if such a path exists and `False` otherwise.
    
5. Final Result: The binary search continues until the left pointer exceeds the right pointer, and the maximum safeness 
    factor is returned as the final result.
'''