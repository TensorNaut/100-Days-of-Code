class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n=len(stoneValue)
        dp=[0]*(n+1)
        for i in range(n-1,-1,-1):
            take=0
            dp[i]=float("-inf")

            for k in range(3):
                if i+k<n:
                    take+=stoneValue[i+k]
                    dp[i]=max(dp[i],take-dp[i+k+1])
        if dp[0]>0:
            return "Alice"
        elif dp[0]<0:
            return "Bob"
        else:
            return "Tie"


#Time Complexity: O(n)
#Space Complexity: O(n)
'''
Approach
1. Create a DP array where dp[i] represents the maximum score difference the current player can achieve starting from index i.
2. Traverse the array from right to left.
3. At every position:
   - Try taking 1, 2, and 3 stones.
   - Calculate the current score.
   - Subtract the opponent's best score difference from the remaining stones.
   - Store the maximum possible score difference.
4. After filling the DP array:
   - If dp[0] > 0, return "Alice".
   - If dp[0] < 0, return "Bob".
   - Otherwise, return "Tie".
'''