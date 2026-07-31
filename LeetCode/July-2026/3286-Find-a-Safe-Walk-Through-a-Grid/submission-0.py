from collections import deque

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])

        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = grid[0][0]

        dq = deque([(0, 0)])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while dq:
            r, c = dq.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    new_cost = dist[r][c] + grid[nr][nc]

                    if new_cost < dist[nr][nc]:
                        dist[nr][nc] = new_cost
                        if grid[nr][nc] == 0:
                            dq.appendleft((nr, nc))
                        else:
                            dq.append((nr, nc))

        return dist[m-1][n-1] < health
    
#Time Complexity: O(m * n)
#Space Complexity: O(m * n)
'''
BFS Approach:
1.  Initialize a distance matrix `dist` to store the minimum cost to reach each cell, starting with infinity.

2.  Set the starting cell (0, 0) cost to its grid value.

3.  Use a deque to perform a BFS traversal of the grid, exploring all four possible directions (up, down, left, right).

4.  For each neighboring cell, calculate the new cost to reach it. If this new cost is less than the previously recorded
    cost, update the distance matrix and add the cell to the deque.

5.  After processing all reachable cells, check if the cost to reach the bottom-right cell (m-1, n-1) is less than 
    the given health. If it is, return True; otherwise, return False.
'''