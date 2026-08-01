class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        memo = {}
        def maxscore(i,j):
            if (i,j) in memo:
                return memo[i,j]
            if i>j:
                return 0
            #
            sA = nums[i] + min( maxscore(i+1,j-1), maxscore(i+2,j  ) ) # pick nums[i] + min of the 2 possible upcoming turns (player 2 is smart)
            sB = nums[j] + min( maxscore(i  ,j-2), maxscore(i+1,j-1) )
            score = max(sA,sB)
            memo[i,j] = score
            return score
        p1 = maxscore(0,len(nums)-1) # Score Player 1
        return p1>=(sum(nums)-p1) # p1 >= p2

#Time Complexity: O(n^2) where n is the length of nums
#Space Complexity: O(n^2) for memoization
'''
Approach:
1.  We define a recursive function `maxscore(i, j)` that calculates the maximum score
    a player can achieve from the subarray `nums[i:j+1]`.
2.  The base case is when `i > j`, which means there are no elements left to pick, so the score is 0.
3.  For each call to `maxscore(i, j)`, we consider two scenarios:
     -  The player picks the leftmost element `nums[i]`, and the opponent will then choose optimally from the remaining elements. 
        The opponent's optimal choice will minimize the player's score, so we take the minimum of the two possible outcomes after the opponent's turn.
     - The player picks the rightmost element `nums[j]`, and similarly, we calculate the minimum score the opponent can force upon the player.
4.  We store the computed scores in a memoization dictionary `memo` to avoid redundant calculations for the same subarray.
5.  Finally, we calculate the score for Player 1 starting from the full array and compare it to Player 2's score 
    (which is the total sum of the array minus Player 1's score). If Player 1's score is greater than or equal to Player 2's score, 
    we return `True`, indicating that Player 1 can win or tie; otherwise, we return `False`.
'''