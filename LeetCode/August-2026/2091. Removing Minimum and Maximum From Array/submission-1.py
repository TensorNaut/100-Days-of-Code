class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        mn, mx = min(nums), max(nums)

        mn_idx = nums.index(mn)
        mx_idx = nums.index(mx)

        return min(
            max(mn_idx, mx_idx) + 1,
            n - min(mn_idx, mx_idx),
            min(mn_idx, mx_idx) + 1 + n - max(mn_idx, mx_idx)
        )

#Time Complexity: O(n)
#Space Complexity: O(1)

'''
Approach:
1. Find the minimum and maximum values in the array.
2. Find the indices of the minimum and maximum values.
3. Calculate the number of deletions required to remove both the minimum and maximum values from the array using three different strategies:
   a. Remove elements from the left side of the array until both minimum and maximum are removed.
   b. Remove elements from the right side of the array until both minimum and maximum are removed.
   c. Remove elements from both sides of the array until both minimum and maximum are removed.
4. Return the minimum number of deletions required among the three strategies.
'''