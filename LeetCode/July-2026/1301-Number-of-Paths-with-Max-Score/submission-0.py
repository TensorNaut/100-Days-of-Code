class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        n = len(board)

        score = [[-1] * n for _ in range(n)]
        ways = [[0] * n for _ in range(n)]

        score[n-1][n-1] = 0
        ways[n-1][n-1] = 1

        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if board[i][j] == 'X' or (i == n-1 and j == n-1):
                    continue
                
                best = -1
                count = 0

                for x, y in ((i+1, j), (i, j+1), (i+1, j+1)):
                    if x<n and y < n and score[x][y] != -1:
                        if score[x][y] > best:
                            best = score[x][y]
                            count = ways[x][y]
                        elif score[x][y] == best:
                            count = (count + ways[x][y]) % MOD

                if best == -1:
                    continue

                value = 0
                if board[i][j].isdigit():
                    value = int(board[i][j])

                score[i][j] = best + value
                ways[i][j] = count
        if ways[0][0] == 0:
            return [0, 0]

        return [score[0][0], ways[0][0] % MOD]


#Time Complexity: O(n^2) where n is the size of the board. We are iterating through each cell of the board once.
#Space Complexity: O(n^2) where n is the size of the board. We are using two 2D arrays to store the score and ways for each cell.

'''
Algorithm Explanation:

1.  We initialize two 2D arrays, `score` and `ways`, to keep
    track of the maximum score and the number of ways to reach each cell, respectively.

2.  We start from the bottom-right corner of the board and iterate backwards to the top-left corner.

3.  For each cell, we check the three possible moves (down, right, and diagonal) and find the maximum score 
    among them.

4.  We also count the number of ways to reach the current cell based on the maximum score

5.  If the current cell is a wall ('X'), we skip it.

6.  Finally, we return the maximum score and the number of ways to reach the top-left corner of the board. 
    If there are no ways to reach it, we return [0, 0].
'''