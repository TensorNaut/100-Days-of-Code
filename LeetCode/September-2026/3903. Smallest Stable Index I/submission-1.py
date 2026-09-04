class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        premax = [0] * n
        sufmax = [0] * n

        premax[0] = nums[0]
        for i in range(1, n):
            premax[i] = max(premax[i-1], nums[i])

        sufmax[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            sufmax[i] = min(sufmax[i+1], nums[i])

        for i in range(n):
            score = premax[i] - sufmax[i]

            if score <= k:
                return i

        return -1


# Time Complexity: O(n)
# Space Complexity: O(n)

'''
Approach:
1. Create a prefixMax array where prefixMax[i] stores the maximum
   value from nums[0] to nums[i].

2. Create a suffixMin array where suffixMin[i] stores the minimum
   value from nums[i] to nums[n-1].

3. For every index i, the instability score can now be calculated
   in O(1) as:
       prefixMax[i] - suffixMin[i]

4. If the score is <= k, return i immediately because we need the
   smallest stable index.

5. If no stable index is found, return -1.
'''