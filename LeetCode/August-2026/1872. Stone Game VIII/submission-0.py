class Solution:
    def stoneGameVIII(self, A: List[int]) -> int:
        n = len(A)
        s = list(accumulate(A))

        @cache
        def maxDiff(i):
            if i == n - 1: return s[n - 1]
            return max(maxDiff(i + 1), s[i] - maxDiff(i + 1))

        return maxDiff(1)


#Time Complexity: O(n)
#Space Complexity: O(n)
'''
Approach:
    1. Use prefix sums to calculate the cumulative sum of the array A.
    2. Define a recursive function maxDiff(i) that returns the maximum difference Alice can achieve starting from index i.
    3. If we are at the last index, return the cumulative sum at that index.
    4. Otherwise, return the maximum of two choices:
        a. Skip the current index and take the result from the next index.
        b. Take the current cumulative sum and subtract the result from the next index.
    5. Use memoization to cache results for efficiency.
    6. Start the recursion from index 1 since Alice must make at least one move.
'''