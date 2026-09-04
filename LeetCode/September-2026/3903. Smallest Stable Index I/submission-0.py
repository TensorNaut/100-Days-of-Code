class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        ans = float('inf')
        for i in range(n):
            score = max(nums[:i+1]) - min(nums[i:])
            if score <= k:
                return i
                
        return -1


# Time Complexity: O(n^2)
# Space Complexity: O(n)
'''
Approach:
1. Iterate through every index i from 0 to n - 1.
2. For each index, find the maximum value in nums[0..i] and
   the minimum value in nums[i..n-1].
3. Calculate the instability score as:
       max(nums[0..i]) - min(nums[i..n-1])
4. If the score is less than or equal to k, return i immediately
   since we are looking for the smallest stable index.
5. If no stable index is found, return -1.
'''