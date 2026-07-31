class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        k %= m*n

        flat = [x for row in grid for x in row]

        l = len(flat)
        
        if k == 0:
            return grid

        res = [(flat[l-k:] + flat[:l-k])[i*n:(i+1)*n] for i in range(m)]

        return res 





#Time Complexity: O(m*n)
#Space Complexity: O(m*n)
'''
Approach:
1.  First, we find the number of rows (m) and columns (n) in the grid.
2.  We then calculate the effective number of shifts needed by taking k modulo (m*n), 
    since shifting the grid m*n times results in the same grid.
3.  We flatten the 2D grid into a 1D list called 'flat'
4.  We then create a new list 'res' by slicing the 'flat' list to get the last k elements and the first (l-k) elements, 
    where l is the length of the flat list.
5.  Finally, we return the reshaped list 'res' as a 2D grid
'''