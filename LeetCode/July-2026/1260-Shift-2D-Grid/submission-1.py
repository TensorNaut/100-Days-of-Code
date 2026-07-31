from collections import deque
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        k %= m*n

        flat = deque([x for row in grid for x in row])

        for i in range(k):
            flat.appendleft(flat.pop())

        res = [list(flat)[i*n:(i+1)*n] for i in range(m)]

        return res 

#Time Complexity: O(m*n)
#Space Complexity: O(m*n)
'''
Approach:
1.  First, we find the number of rows (m) and columns (n) in the grid.
2.  We then calculate the effective number of shifts needed by taking k modulo (m*n),
    since shifting the grid m*n times results in the same grid.
3.  We flatten the 2D grid into a 1D deque called 'flat'
4.  We then perform k shifts by popping the last element of the deque and appending it to the front of the deque.
5.  Finally, we return the reshaped list 'res' as a 2D grid by slicing the deque into rows of length n.
'''