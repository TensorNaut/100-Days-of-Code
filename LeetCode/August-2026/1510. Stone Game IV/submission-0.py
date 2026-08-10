class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # dp[i] = True if the current player can win
        # when there are i stones
        dp = [False] * (n + 1)

        for i in range(1, n + 1):
            square = 1

            while square * square <= i:
                # If removing this square leaves a losing position,
                # then the current player can win.
                if dp[i - square * square] == False:
                    dp[i] = True
                    break

                square += 1

        return dp[n]



#Time Complexity: O(n√n)
#Space Complexity: O(n)

'''
Approach
- Use dp[i] to represent whether the player whose turn it is can win when there are i stones.
- For every i, try removing every possible square number: 1, 4, 9, 16, ....
- If removing a square leaves the opponent in a losing position (dp[...] == False), then the current player can win.
- Finally, return dp[n], which tells us whether Alice can win starting with n stones
'''