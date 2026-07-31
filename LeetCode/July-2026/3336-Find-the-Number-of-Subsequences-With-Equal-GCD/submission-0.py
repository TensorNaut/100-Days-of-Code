from math import gcd
from typing import List

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        MAX = 200

        # Precompute gcd transitions
        nxt = [[0] * (MAX + 1) for _ in range(MAX + 1)]
        for g in range(MAX + 1):
            for x in range(1, MAX + 1):
                nxt[g][x] = x if g == 0 else gcd(g, x)

        dp = [[0] * (MAX + 1) for _ in range(MAX + 1)]
        dp[0][0] = 1

        for x in nums:
            ndp = [row[:] for row in dp]  # option: skip

            for g1 in range(MAX + 1):
                for g2 in range(MAX + 1):
                    cur = dp[g1][g2]
                    if cur == 0:
                        continue

                    # Put x into seq1
                    ng1 = nxt[g1][x]
                    ndp[ng1][g2] = (ndp[ng1][g2] + cur) % MOD

                    # Put x into seq2
                    ng2 = nxt[g2][x]
                    ndp[g1][ng2] = (ndp[g1][ng2] + cur) % MOD

            dp = ndp

        ans = 0
        for g in range(1, MAX + 1):
            ans = (ans + dp[g][g]) % MOD

        return ans
    

#Time Complexity: O(n * MAX^2), where n is the length of the input list nums and MAX is the maximum value in nums (200 in this case). The nested loops iterate over all possible GCD values for both sequences.
#Space Complexity: O(MAX^2), as we maintain a 2D dp array of size (MAX + 1) x (MAX + 1) to store the counts of subsequences with specific GCD values.

'''
Approach:
1.  Precompute the GCD transitions for all pairs of numbers up to MAX (200 in this case). 
    This allows us to quickly determine the new GCD when adding a number to a subsequence.

2.  Initialize a 2D dynamic programming (dp) array where dp[g1][g2] represents the count of 
    subsequences with GCD g1 for the first sequence and GCD g2 for the second sequence.

3.  Iterate through each number in the input list nums. For each number, create a new dp array (ndp) 
    to store the updated counts after considering the current number.

4.  For each possible GCD pair (g1, g2), update the counts in ndp by considering three options: 
    skipping the current number, adding it to the first sequence, or adding it to the second sequence. 
    Use the precomputed GCD transitions to determine the new GCD values.

5.  After processing all numbers, sum the counts of subsequences where both sequences have the same GCD (g1 == g2)
    to get the final answer.

6.  Return the final answer modulo 10^9 + 7 to handle large numbers.
'''