from collections import deque

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:

        m = len(classroom)
        n = len(classroom[0])

        # Find S and give every L an index
        litter = {}
        start = None
        count = 0

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start = (i, j)

                elif classroom[i][j] == 'L':
                    litter[(i, j)] = count
                    count += 1

        # All litter already collected
        if count == 0:
            return 0

        # mask = which litter has been collected
        all_mask = (1 << count) - 1

        # BFS state:
        # (row, col, remaining_energy, mask, moves)
        q = deque()
        q.append((start[0], start[1], energy, 0, 0))

        # States we have already visited
        visited = set()
        visited.add((start[0], start[1], energy, 0))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:

            r, c, e, mask, moves = q.popleft()

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                # Outside the grid
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                # Obstacle
                if classroom[nr][nc] == 'X':
                    continue

                # Need energy to make a move
                if e == 0:
                    continue

                # Spend 1 energy
                ne = e - 1
                nmask = mask

                # Collect litter
                if (nr, nc) in litter:
                    bit = litter[(nr, nc)]
                    nmask |= (1 << bit)

                # Reset energy
                if classroom[nr][nc] == 'R':
                    ne = energy

                # All litter collected
                if nmask == all_mask:
                    return moves + 1

                state = (nr, nc, ne, nmask)

                if state not in visited:
                    visited.add(state)
                    q.append((nr, nc, ne, nmask, moves + 1))

        return -1


#Time Complexity: O(m * n * 2^k) where m is the number of rows, n is the number of columns, and k is the number of litter pieces. This is because we can have at most m * n positions and 2^k possible states for the litter collection.
#Space Complexity: O(m * n * 2^k) for the visited set and the queue used in BFS.

'''
Approach:
1. Parse the classroom grid to find the starting position 'S' and all litter positions 'L'. Assign each litter position a unique index for bitmasking.
2. Use a breadth-first search (BFS) to explore all possible moves from the starting position. Each state in the BFS will include the current position, remaining energy, collected litter mask, and the number of moves taken.
3. For each move, check if the new position is valid (within bounds and not an obstacle 'X'). If the position contains litter, update the collected litter mask. If the position is a recharge station 'R', reset the energy to the initial value.
4. If all litter has been collected (i.e., the collected litter mask equals the all_mask), return the number of moves taken. If the queue is exhausted without collecting all litter, return -1.
'''